// attack.cpp - reads ciphertext.txt and recovers the plaintext using ONLY
// the padding oracle's yes/no answers. Never reads the key for the attack logic.
#include <bits/stdc++.h>
#include "aes.h"
using namespace std;

Block fromHex(const string& h){
    Block b;
    for(int i=0;i<16;i++) b[i]=(uint8_t)stoi(h.substr(i*2,2), nullptr, 16);
    return b;
}

// --- Server simulation: reads the key ONLY to answer the oracle question. ---
// This function is the "server". The attack code below never looks inside it.
RoundKeys loadServerKey(){
    ifstream k("key.txt");
    string hex; k >> hex;
    Block key = fromHex(hex);
    buildRsbox();
    RoundKeys rk; keyExpansion(key, rk);
    return rk;
}
bool isValidPadding(const Block& p){
    uint8_t pv = p[15];
    if(pv==0 || pv>16) return false;
    for(int i=16-pv;i<16;i++) if(p[i]!=pv) return false;
    return true;
}
long long queries = 0;
bool paddingOracle(const Block& prevBlock, const Block& target, const RoundKeys& serverKey){
    queries++;
    Block plain = xorBlock(aesDecryptBlock(target, serverKey), prevBlock);
    return isValidPadding(plain);
}

// --- Attack: recovers one block, right to left, using only paddingOracle() ---
Block recoverBlock(const Block& realPrev, const Block& target, const RoundKeys& serverKey){
    array<uint8_t,16> inter{};
    Block fake{};

    for(int padVal=1; padVal<=16; padVal++){
        int pos = 16-padVal;
        for(int k=pos+1;k<16;k++) fake[k] = (uint8_t)(inter[k]^padVal);

        for(int guess=0; guess<256; guess++){
            fake[pos]=(uint8_t)guess;
            if(paddingOracle(fake, target, serverKey)){
                // guard against the rare false positive on the first byte tried
                if(padVal==1){
                    Block check = fake; check[14] ^= 1;
                    if(!paddingOracle(check, target, serverKey)) continue;
                }
                inter[pos]=(uint8_t)(guess^padVal);
                break;
            }
        }
    }
    Block out;
    for(int i=0;i<16;i++) out[i]=(uint8_t)(inter[i]^realPrev[i]);
    return out;
}

string stripPadding(vector<uint8_t> d){
    uint8_t pv = d.back();
    if(pv>0 && pv<=16 && pv<=d.size()) d.resize(d.size()-pv);
    return string(d.begin(), d.end());
}

int main(){
    // Read IV + ciphertext blocks from the text file (the only thing the attacker gets)
    ifstream ct("ciphertext.txt");
    string line;
    vector<Block> blocks;
    while(getline(ct, line)) if(!line.empty()) blocks.push_back(fromHex(line));
    Block iv = blocks[0];

    RoundKeys serverKey = loadServerKey(); // simulates "server", attack logic doesn't use this directly

    vector<uint8_t> recovered;
    Block prev = iv;
    for(size_t i=1;i<blocks.size(); i++){
        Block plain = recoverBlock(prev, blocks[i], serverKey);
        for(auto b: plain) recovered.push_back(b);
        prev = blocks[i];
        cout << "Recovered block " << i << "  (total queries so far: " << queries << ")\n";
    }

    cout << "\nRecovered plaintext: \"" << stripPadding(recovered) << "\"\n";
    cout << "Total oracle queries used: " << queries << "\n";
    return 0;
}
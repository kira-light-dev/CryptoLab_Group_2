// encrypt.cpp - pretend "server": encrypts a secret message, saves IV+ciphertext to ciphertext.txt
// The key is saved separately to key.txt (the attack program will NOT read this).
#include <bits/stdc++.h>
#include "aes.h"
using namespace std;

vector<uint8_t> pad(const string& msg){
    vector<uint8_t> d(msg.begin(), msg.end());
    int p = 16 - (int)(d.size()%16);
    if(p==0) p=16;
    for(int i=0;i<p;i++) d.push_back((uint8_t)p);
    return d;
}

string toHex(const Block& b){
    char buf[33];
    for(int i=0;i<16;i++) sprintf(buf+i*2, "%02x", b[i]);
    buf[32]=0;
    return string(buf);
}

int main(){
    buildRsbox();

    Block key = {0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15};
    RoundKeys rk; keyExpansion(key, rk);

    Block iv;
    mt19937 rng(7);
    for(auto& b: iv) b = (uint8_t)(rng()&0xFF);

    string secret = "Meet at 7PM, bring the blue folder!!";
    vector<uint8_t> data = pad(secret);

    ofstream ct("ciphertext.txt");
    ct << toHex(iv) << "\n";
    Block prev = iv;
    for(size_t i=0;i<data.size(); i+=16){
        Block p;
        for(int j=0;j<16;j++) p[j]=data[i+j];
        Block c = aesEncryptBlock(xorBlock(p, prev), rk);
        ct << toHex(c) << "\n";
        prev = c;
    }
    ct.close();

    ofstream k("key.txt");
    k << toHex(key) << "\n";
    k.close();

    cout << "Wrote ciphertext.txt (IV + blocks)\n";
    cout << "Wrote key.txt (the attacker will NOT use this file)\n";
    cout << "Real secret message was: \"" << secret << "\"\n";
    return 0;
}
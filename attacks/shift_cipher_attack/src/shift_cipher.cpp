#include <bits/stdc++.h>
using namespace std;

int main(){
    set<string> dictionary;
    ifstream dictFile("../dictionary/dict.txt");
    if(!dictFile){
        cout << "Could not open dict.txt\n";
        return 1;
    }
    string word;
    while(dictFile >> word) dictionary.insert(word);
    dictFile.close();

    cout << "Enter cipher sentence (lowercase, spaces allowed): ";
    string line;
    getline(cin, line);

    for(int shift = 0; shift < 26; shift++){
        string decoded = line;
        for(char &c : decoded){
            if(c >= 'a' && c <= 'z')
                c = 'a' + (c - 'a' - shift + 26) % 26;
        }

        stringstream ss(decoded);
        string w;
        int matches = 0, total = 0;
        while(ss >> w){
            total++;
            if(dictionary.count(w)) matches++;
        }

        cout << "Shift " << shift << ": " << decoded
             << "   (" << matches << "/" << total << " valid words)\n";
    }

    return 0;
}
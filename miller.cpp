#include <bits/stdc++.h>
using namespace std;

long long modpow(long long base, long long exp, long long mod) {
    long long result = 1;
    base %= mod;
    while (exp > 0) {
        if (exp & 1)
            result = (__int128)result * base % mod;
        base = (__int128)base * base % mod;
        exp >>= 1;
    }
    return result;
}

bool millerTest(long long n, long long d) {

    long long a = 2 + rand() % (n - 3);   

    long long x = modpow(a, d, n);

    if (x == 1 || x == n - 1)
        return true;

    while (d != n - 1) {
        x = (__int128)x * x % n;
        d *= 2;

        if (x == 1) return false;      
        if (x == n - 1) return true;    
    }

    return false;  
}

bool isPrime(long long n, int k) {

    if (n <= 1) return false;
    if (n <= 3) return true;

    if (n % 2 == 0) return false;

    long long d = n - 1;
    while (d % 2 == 0)
        d /= 2;

    for (int i = 0; i < k; i++) {
        if (!millerTest(n, d))
            return false;
    }

    return true;
}

int main() {
    srand((unsigned)time(nullptr));

    int k = 10;  

    vector<long long> testNumbers = {
        2, 17, 561, 997, 100000, 999999937, 7919
    };

    cout << "Testing isPrime() on sample numbers (k=" << k << " rounds):\n\n";
    for (long long n : testNumbers) {
        cout << n << " -> " << (isPrime(n, k) ? "PRIME" : "COMPOSITE") << "\n";
    }

    cout << "\nSearching for a random prime between 10,000 and 100,000...\n";
    long long candidate;
    do {
        candidate = 10000 + rand() % 90000;
        if (candidate % 2 == 0) candidate++; 
    } while (!isPrime(candidate, k));

    cout << "Found prime: " << candidate << "\n";

    return 0;
}
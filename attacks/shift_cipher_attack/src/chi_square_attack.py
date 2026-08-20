from shift_cipher import decrypt

ENGLISH_FREQ = {
    'a': 8.167, 'b': 1.492, 'c': 2.782, 'd': 4.253, 'e': 12.702,
    'f': 2.228, 'g': 2.015, 'h': 6.094, 'i': 6.966, 'j': 0.153,
    'k': 0.772, 'l': 4.025, 'm': 2.406, 'n': 6.749, 'o': 7.507,
    'p': 1.929, 'q': 0.095, 'r': 5.987, 's': 6.327, 't': 9.056,
    'u': 2.758, 'v': 0.978, 'w': 2.360, 'x': 0.150, 'y': 1.974,
    'z': 0.074
}

def chi_square_score(text):
    counts = {chr(97 + i): 0 for i in range(26)}
    for ch in text:
        if 'a' <= ch <= 'z':
            counts[ch] += 1

    n = sum(counts.values())
    if n == 0:
        return float("inf")

    chi2 = 0
    for letter, observed in counts.items():
        expected = ENGLISH_FREQ[letter] / 100 * n
        if expected > 0:
            chi2 += ((observed - expected) ** 2) / expected
    return chi2

def chi_square_attack(ciphertext):
    best_key = -1
    best_score = float("inf")
    best_decoded = ""

    for key in range(26):
        decoded = decrypt(ciphertext, key)
        score = chi_square_score(decoded)
        if score < best_score:
            best_score = score
            best_key = key
            best_decoded = decoded

    return best_key, best_decoded, best_score
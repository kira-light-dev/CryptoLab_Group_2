"""
chi_square_attack.py
Cryptanalysis Algorithm 2: Chi-Square Statistical Attack

Idea:
  - English text has a well-known letter frequency distribution
    (e.g. 'e' is the most common letter, ~12.7%, 'z' is rare, ~0.07%).
  - A Shift Cipher just rotates the alphabet, so the ciphertext's
    letter-frequency histogram is the SAME shape as English, just
    rotated by the key.
  - For each candidate key (0-25):
        1. Decrypt with that key.
        2. Count letter frequencies of the result.
        3. Compute a Chi-Square statistic comparing observed
           frequencies to expected English frequencies:
               chi2 = sum( (observed_i - expected_i)^2 / expected_i )
  - The key with the LOWEST chi-square score is the best match
    to real English letter statistics -> predicted key.

Unlike the dictionary attack, this does NOT need whole words to
match anything -- it works purely on statistical letter shape,
so it can still work even with typos or an incomplete dictionary.
"""

from shift_cipher import decrypt

# Standard English letter frequency (%) - Source: common cryptanalysis references
ENGLISH_FREQ = {
    'a': 8.167, 'b': 1.492, 'c': 2.782, 'd': 4.253, 'e': 12.702,
    'f': 2.228, 'g': 2.015, 'h': 6.094, 'i': 6.966, 'j': 0.153,
    'k': 0.772, 'l': 4.025, 'm': 2.406, 'n': 6.749, 'o': 7.507,
    'p': 1.929, 'q': 0.095, 'r': 5.987, 's': 6.327, 't': 9.056,
    'u': 2.758, 'v': 0.978, 'w': 2.360, 'x': 0.150, 'y': 1.974,
    'z': 0.074
}


def letter_counts(text: str) -> dict:
    counts = {chr(ord('a') + i): 0 for i in range(26)}
    for ch in text:
        if 'a' <= ch <= 'z':
            counts[ch] += 1
    return counts


def chi_square_score(text: str) -> float:
    """Lower score = closer to real English letter distribution."""
    counts = letter_counts(text)
    n = sum(counts.values())
    if n == 0:
        return float("inf")

    chi2 = 0.0
    for letter, observed in counts.items():
        expected = ENGLISH_FREQ[letter] / 100.0 * n
        if expected > 0:
            chi2 += ((observed - expected) ** 2) / expected
    return chi2


def chi_square_attack(ciphertext: str):
    """
    Try all 26 shifts, score each with chi-square against English
    letter frequencies. Returns (best_key, best_decoded, all_results)
    where all_results = list of (key, decoded, chi2_score).
    """
    best_key = -1
    best_score = float("inf")
    best_decoded = ""
    all_results = []

    for key in range(26):
        decoded = decrypt(ciphertext, key)
        score = chi_square_score(decoded)
        all_results.append((key, decoded, score))

        if score < best_score:
            best_score = score
            best_key = key
            best_decoded = decoded

    return best_key, best_decoded, all_results


if __name__ == "__main__":
    cipher = "wkh nlqj dqg txhhq frph dw gdzq"  # shift 3

    key, decoded, results = chi_square_attack(cipher)

    for k, dec, score in results:
        print(f"Key {k:2d}: {dec}   (chi2 = {score:.2f})")

    print("\n--- Chi-Square Attack Result ---")
    print(f"Predicted key : {key}")
    print(f"Decoded text  : {decoded}")
    print(f"Chi-square    : {results[key][2]:.2f}")
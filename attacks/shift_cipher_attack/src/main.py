from shift_cipher import encrypt
from chi_square_attack import chi_square_attack

plaintext = "the king and queen come at dawn"
key = 3

ciphertext = encrypt(plaintext, key)
print("Plaintext :", plaintext)
print("Key used  :", key)
print("Ciphertext:", ciphertext)

pred_key, decoded, score = chi_square_attack(ciphertext)

print("\n--- Chi-Square Attack Result ---")
print("Predicted key:", pred_key)
print("Decoded text :", decoded)
print("Chi-square   :", round(score, 2))
print("Correct?     :", pred_key == key)
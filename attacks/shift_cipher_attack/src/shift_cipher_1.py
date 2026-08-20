def crack_caesar():
    try:
        with open("dict.txt", "r") as f:
            dictionary = set(f.read().split())
    except FileNotFoundError:
        print("Could not open dict.txt")
        return

    line = input("Enter cipher sentence (lowercase, spaces allowed): ")

    best_shift = -1
    best_matches = -1
    best_total = 0
    best_decoded = ""

    for shift in range(26):
        decoded_chars = []
        for c in line:
            if 'a' <= c <= 'z':
                decoded_chars.append(chr((ord(c) - ord('a') - shift) % 26 + ord('a')))
            else:
                decoded_chars.append(c)
        decoded = "".join(decoded_chars)

        words = decoded.split()
        total = len(words)
        matches = sum(1 for w in words if w in dictionary)

        print(f"Shift {shift}: {decoded}   ({matches}/{total} valid words)")

        if matches > best_matches:
            best_matches = matches
            best_total = total
            best_shift = shift
            best_decoded = decoded

    print("\n--- Best Match ---")
    print(f"Key (shift): {best_shift}")
    print(f"Decoded: {best_decoded}")
    print(f"Valid words: {best_matches}/{best_total}")

if __name__ == "__main__":
    crack_caesar()
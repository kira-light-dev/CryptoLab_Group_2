def encrypt(text, key):
    text = text.lower()
    result = ""
    for ch in text:
        if 'a' <= ch <= 'z':
            result += chr((ord(ch) - ord('a') + key) % 26 + ord('a'))
        else:
            result += ch
    return result

def decrypt(text, key):
    text = text.lower()
    result = ""
    for ch in text:
        if 'a' <= ch <= 'z':
            result += chr((ord(ch) - ord('a') - key) % 26 + ord('a'))
        else:
            result += ch
    return result
def decipher(encoded_str):
    decoded_str = ""
    for char in encoded_str:
        if 'a' <= char <= 'z':
            decoded_str += chr((ord(char) - ord('a') + 13) % 26 + ord('a'))
        elif 'A' <= char <= 'Z':
            decoded_str += chr((ord(char) - ord('A') + 13) % 26 + ord('A'))
        else:
            decoded_str += char
    return decoded_str

# Encoded String
encoded_message = "Gur pyrnare gur zbafgref, gur orggre gur rkcynangvba."

def main():
    decoded_message = decipher(encoded_message)
    print("Decoded Message:", decoded_message)

if __name__ == "__main__":
    main()

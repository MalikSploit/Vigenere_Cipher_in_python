# We need the Alphabet because we convert letters into numerical values
# So that we can use mathematical operation (note we encrypt the spaces as well)
ALPHABET = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ' 

def vigenere_encrypt(plain_text, key):
    # This is the text we want to encrypt + case-insensitive
    plain_text = plain_text.upper()
    key = key.upper()
    cipher_text = ''
    # It represents the index of the letters of the key
    key_index = 0

    # We have to consider all the characters in the plain_text
    for character in plain_text:
        # Number of shitfs = index of the character in the alphabet + index of the character in the key
        index = (ALPHABET.find(character) + ALPHABET.find(key[key_index])) % len(ALPHABET)
        # Key appending the encrypted character to the cipher_text
        cipher_text = cipher_text + ALPHABET[index]
        # Increment the key index because we consider the next letter
        key_index = key_index + 1
        # If we have considered the last letter of the key we start again
        if key_index == len(key):
            key_index = 0

    return cipher_text


def vigenere_decrypt(cipher_text, key):
    # This is the cipher_text we want to decrypt 
    cipher_text = cipher_text.upper()
    key = key.upper()
    plain_text = ''
    # It represents the index of the letters of the key
    key_index = 0

    # We have to consider all the characters in the cipher_text
    for character in cipher_text:
        # Number of shitfs = index of the character in the alphabet - index of the character in the key
        index = (ALPHABET.find(character) - ALPHABET.find(key[key_index])) % len(ALPHABET)
        # Key appending the encrypted character to the plain_text
        plain_text = plain_text + ALPHABET[index]
        key_index = key_index + 1
        if key_index == len(key):
            key_index = 0

    return plain_text


if __name__ == '__main__':
    text = 'CRYPTOGRAPHY IS QUITE IMPORTANT IN CRYPTOCURRENCIES'
    cipher = vigenere_encrypt(text, 'Malik')
    print("The encrypted message is : %s\n" % cipher)
    print("The decrypted message is : %s\n" % vigenere_decrypt(cipher, 'Malik'))


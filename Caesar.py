import string

# Listing the alphabets for encryption
# There are 26 letters, from index 0 to 25
lower_alphabet = list(string.ascii_lowercase)
upper_alphabet = list(string.ascii_uppercase)

# Getting the key input
key = 0
while key <= 0:
    key = int(input("Enter the caesar key: "))

# Getting the text to encrypt
text = str(input("Enter the plane text to encrypt: "))

# Encryption
for letter in text:
    # Check if letter is lower
    if letter in lower_alphabet:
        # Applying the key
        enc_letter = lower_alphabet.index(letter) + key
        # Cycling the key
        if enc_letter > 25:
            enc_letter = 0 + (enc_letter - 26)
            print(lower_alphabet[enc_letter], end="")
        elif 0 <= enc_letter <= 25:
            print(lower_alphabet[enc_letter], end="")
    elif letter in upper_alphabet:
        # Applying the key
        enc_letter = upper_alphabet.index(letter) + key
        # Cycling the key
        if enc_letter > 25:
            enc_letter = 0 + (enc_letter - 26)
            print(upper_alphabet[enc_letter], end="")
        elif 0 <= enc_letter <= 25:
            print(upper_alphabet[enc_letter], end="")
    # Printing anything thats not a letter normally
    else:
        print(letter, end="")

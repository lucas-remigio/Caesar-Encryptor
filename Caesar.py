import string

low_alpha = list(string.ascii_lowercase)                        # Listing the alphabets
upp_alpha = list(string.ascii_uppercase)                        # There are 26 letters, index 0 => 25

key = 0
while key <= 0:                                                 # Getting the key input
    key = int(input("Enter the caesar key: "))

text = str(input("Enter the plane text to encrypt: "))          # Getting the text to encrypt


# Encryption

for letter in text:
    if letter in low_alpha:                                     # Check if letter is lower
        enc_l = low_alpha.index(letter) + key                   # Applying the key
        if enc_l > 25:                                          # Cycling the key
            enc_l = 0 + (enc_l - 26)
            print(low_alpha[enc_l], end="")
        elif 0 <= enc_l <= 25:
            print(low_alpha[enc_l], end="")
    elif letter in upp_alpha:                                   # Check if letter is upper
        enc_l = upp_alpha.index(letter) + key                   # Applying the key
        if enc_l > 25:                                          # Cycling the key
            enc_l = 0 + (enc_l - 26)
            print(upp_alpha[enc_l], end="")
        elif 0 <= enc_l <= 25:
            print(upp_alpha[enc_l], end="")
    else:
        print(letter, end="")                                   # Printing anything thats not a letter

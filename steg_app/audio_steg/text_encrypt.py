def text_encrypt(plaintext, hiddentext):
    encrypted_text = ""
    encrypted_text = plaintext + encrypted_text
    for i in hiddentext:
        whitespacecount = ord(i) - 31 # to save space 
        whitespacelist = [" "]*whitespacecount
        encrypted_text = encrypted_text + ''.join(whitespacelist) + '\t'
    return encrypted_text

def text_decrypt(encrypted_text):
    decrypted_text = ""
    whitespacecount = 0
    cipher_text = encrypted_text[0:len(encrypted_text)] #remove end character
    for i in encrypted_text:
        if i == '\t':
            decrypted_text = decrypted_text + chr(whitespacecount + 31) 
            whitespacecount = 0
        elif i.isspace():
            whitespacecount = whitespacecount + 1
        elif i.isalpha():
            whitespacecount = 0
            continue
    return decrypted_text


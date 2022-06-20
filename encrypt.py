

def encrypt(text: str) -> str:
    encrypted_text = ""
    for char in text:
        ascii_decimal = ord(char) + 5
        encrypted_text += chr(ascii_decimal)
    return encrypted_text


def decrypt(encrypted_text: str) -> str:
    decrypted_text = ""
    for char in encrypted_text:
        ascii_decimal = ord(char) - 5
        decrypted_text += chr(ascii_decimal)
    return decrypted_text
def encrypt(num_steps: int, text: str) -> str:
    """
    Encrypt a text using Caesar cypher method

    args:
        num_steps (int): how many unicode positions ahead the cypher will encrypt
        text (str): the piece of text you want to encrypt

    returns:
        str: the given text encrypted
    """

    if type(num_steps) is not int or type(text) is not str:
        raise TypeError('Argument(s) not of correct type. Please re-check and try again.')

    encrypted_text = ""
    for char in text:
        ascii_decimal = ord(char) + num_steps
        encrypted_text += chr(ascii_decimal)
    return encrypted_text


def decrypt(num_steps: int, encrypted_text: str) -> str:
    """
    Decrypts a text using Caesar cypher method

    args:
        num_steps (int): how many unicode positions down the cypher will decrypt
        encrypted_text (str): the encrypted piece of text you want to decrypt

    returns:
        str: the given encrypted text decrypted
    """

    if type(num_steps) is not int or type(encrypted_text) is not str:
        raise TypeError('Argument(s) not of correct type. Please re-check and try again.')

    decrypted_text = ""
    for char in encrypted_text:
        ascii_decimal = ord(char) - num_steps
        decrypted_text += chr(ascii_decimal)
    return decrypted_text
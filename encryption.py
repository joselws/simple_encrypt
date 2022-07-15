import os

def encrypt(key: int, message: str) -> str:
    """
    Encrypt a text using Caesar cypher method

    args:
        key (int): how many unicode positions ahead the cypher will encrypt
        message (str): the piece of text you want to encrypt

    returns:
        str: the given text encrypted
    """

    if type(key) is not int or type(message) is not str:
        raise TypeError('Argument(s) not of correct type. Please re-check and try again.')

    encrypted_text = ""
    for character in message:
        ascii_decimal = ord(character) + key
        encrypted_text += chr(ascii_decimal)
    return encrypted_text


def decrypt(key: int, encrypted_message: str) -> str:
    """
    Decrypts a text using Caesar cypher method

    args:
        key (int): how many unicode positions down the cypher will decrypt
        encrypted_message (str): the encrypted piece of text you want to decrypt

    returns:
        str: the given encrypted text decrypted
    """

    if type(key) is not int or type(encrypted_message) is not str:
        raise TypeError('Argument(s) not of correct type. Please re-check and try again.')

    decrypted_text = ""
    for character in encrypted_message:
        ascii_decimal = ord(character) - key
        decrypted_text += chr(ascii_decimal)
    return decrypted_text

def get_cli_parameters(cli_parameters: list) -> tuple:
    """
    Helper function for encrypt_file and decrypt_file programs.
    Handles the validation and extraction of CLI parameters

    Args:
        cli_parameters (list): originated by passing in sys.argv,
            takes the first three arguments which are:
            int: key of the encryption/decryption process
            str: input filename

    Returns:
        tuple (int, str): the two arguments described above
    """

    try:
        key = int(cli_parameters[1])
        filename = cli_parameters[2]
    except IndexError:
        print("Not enough parameters given.")
        raise
    except ValueError:
        print("Key must be an integer.")
        raise
    except:
        print("Uncatched error.")
        raise
    else:
        if not filename:
            print("Input filenames can't be empty.")
            raise ValueError
    
        if not os.path.exists(filename):
            print(f"File {filename} does not exist.")
            raise FileNotFoundError

        return key, filename
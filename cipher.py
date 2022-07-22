import os
from exceptions import CLIParamsError, CipherError

def cipher(action: str, key: int, message: str) -> str:
    """
    Cipher (encrypt or decrypt) a message given a key

    args:
        action (str): "encrypt" or "decrypt" possible values
        key (int): how many unicode positions ahead the cipher will encrypt
        message (str): the piece of text you want to encrypt

    returns:
        str: the given text ciphered
    """

    if type(key) is not int or type(message) is not str:
        raise TypeError('Argument(s) not of correct type. Please re-check and try again.')

    encrypted_text = ""
    for character in message:
        ascii_decimal = ord(character) + key
        encrypted_text += chr(ascii_decimal)
    return encrypted_text

def get_cli_parameters(cli_parameters: list) -> tuple:
    """
    Helper function for cipher_file program.
    Handles the validation and extraction of CLI parameters

    Args:
        cli_parameters (list): originated by passing in sys.argv,
        takes the first three arguments which are:
            str: 'encrypt' or 'decrypt' action
            int: key of the cipher process
            list[str]: filenames of files you want to cipher

    Returns:
        tuple (str, int, list[str]): all arguments described above in a tuple
    """

    if len(cli_parameters) < 3:
        raise CLIParamsError(f"CLI parameters provided less than 3: {len(cli_parameters)}")

    action = cli_parameters[0]
    if action not in ["encrypt", "decrypt"]:
        raise CLIParamsError(f"Action type invalid '{action}'.")

    try:
        key = int(cli_parameters[1])
    except ValueError as e:
        raise ValueError(f"Key value '{cli_parameters[1]}' must be a positive number.") from e
    else:
        if key <= 0:
            raise CLIParamsError(f"Key value {key} must be a positive number.")

    filenames = cli_parameters[2:]
    for filename in filenames:
        if not os.path.exists(filename):
            raise FileNotFoundError(f"File {filename} not found.")

    return (action, key, filenames)
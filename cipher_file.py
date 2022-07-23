from cipher import cipher, get_cli_parameters
from exceptions import CipherFileError
import sys


def main() -> None:
    """
    Cipher an existing input file given correct CLI arguments
    Execute by calling: 
        python3 cipher_file.py <action> <key> <filename1> ... <filename_n>

    CLI args:
        action (str): "encrypt" or "decrypt"
        key (int): number of steps <filenames> will be ciphered
        filenames (many str): names of existing files with the content you want to cipher
    """

    if len(sys.argv) < 4:
        raise CipherFileError("Not enough CLI parameters.")

    try:
        action, key, filenames = get_cli_parameters(sys.argv[1:])
    except CipherFileError as e:
        raise CipherFileError(f'Uncatched error {e}') from e

    for filename in filenames:
        with open(filename) as input_file:
            text = input_file.read()

        ciphered_content = cipher(action, key, text)

        with open(filename, 'w') as file:
            file.write(ciphered_content)
    

if __name__ == '__main__':
    main()
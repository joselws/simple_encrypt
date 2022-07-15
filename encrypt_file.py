from encryption import encrypt, get_cli_parameters
import sys


def encrypt_file() -> None:
    """
    Encrypt an existing input file given correct CLI arguments
    Execute by calling: 
        python3 encrypt_file.py <key> <filename>

    CLI args:
        key (int): number of steps ahead <filename> will be encrypted
        filename (str): name of an existing file with the content you want to encrypt
    """

    try:
        key, filename = get_cli_parameters(sys.argv)
    except:
        print('Terminating program')
        return

    with open(filename) as input_file:
        input_contents = input_file.read()

    encrypted_content = encrypt(key, input_contents)

    with open(filename, 'w') as file:
        file.write(encrypted_content)
    

if __name__ == '__main__':
    encrypt_file()
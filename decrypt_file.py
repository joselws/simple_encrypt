from encryption import decrypt, get_cli_parameters
import sys


def decrypt_file() -> None:
    """
    Decrypt an existing encrypted input file given correct CLI arguments
    Execute by calling: 
        python3 decrypt_file.py <key> <filename>

    CLI args:
        key (int): number of steps behind that <filename> will be decrypted
        filename (str): name of an existing encrypted file with the content you want to decrypt
    """

    try:
        key, filename = get_cli_parameters(sys.argv)
    except:
        print('Terminating program')
        return

    with open(filename) as input_file:
        input_contents = input_file.read()

    decrypted_content = decrypt(key, input_contents)

    with open(filename, 'w') as file:
        file.write(decrypted_content)
    

if __name__ == '__main__':
    decrypt_file()
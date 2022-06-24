from encryption import encrypt, get_cli_parameters
import sys


def encrypt_file() -> None:
    """
    Encrypt an existing input file in a new output file given correct CLI arguments
    Execute by calling: 
        python3 encrypt_file.py <num_steps> <input_file> <output_file>

    CLI args:
        num_steps (int): number of steps ahead <input_file> will be encrypted
        input_file (str): name of an existing file with the content you want to encrypt
        output_file (str): name of the output file name with the encrypted content of input_file
    """

    try:
        num_steps, input_filename, output_filename = get_cli_parameters(sys.argv)
    except:
        print('Terminating program')
        return

    with open(input_filename) as input_file:
        input_contents = input_file.read()

    encrypted_content = encrypt(num_steps, input_contents)

    with open(output_filename, 'w') as output_file:
        output_file.write(encrypted_content)
    

if __name__ == '__main__':
    encrypt_file()
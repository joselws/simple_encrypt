from encryption import decrypt, get_cli_parameters
import sys


def decrypt_file() -> None:
    """
    Decrypt an existing encrypted input file in a new output file given correct CLI arguments
    Execute by calling: 
        python3 decrypt_file.py <num_steps> <input_file> <output_file>

    CLI args:
        num_steps (int): number of steps behind that <input_file> will be decrypted
        input_file (str): name of an existing encrypted file with the content you want to decrypt
        output_file (str): name of the output file name with the decrypted content of input_file
    """

    try:
        num_steps, input_filename, output_filename = get_cli_parameters(sys.argv)
    except:
        print('Terminating program')
        return

    with open(input_filename) as input_file:
        input_contents = input_file.read()

    decrypted_content = decrypt(num_steps, input_contents)

    with open(output_filename, 'w') as output_file:
        output_file.write(decrypted_content)
    

if __name__ == '__main__':
    decrypt_file()
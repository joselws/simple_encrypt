from encryption import encrypt, decrypt, get_cli_parameters
from encrypt_file import encrypt_file
import os
import unittest


class TestEncryption(unittest.TestCase):
    """Tests for encryption module"""

    def tearDown(self):
        """Delete test encrypted and decrypted files"""

        encrypted_filename = 'test_encrypted_text.txt'
        decrypted_filename = 'test_decrypted_text.txt'

        if os.path.exists(encrypted_filename):
            os.remove(encrypted_filename)

        if os.path.exists(decrypted_filename):
            os.remove(decrypted_filename)
    

    def test_encrypt(self):
        """Encrypt method works correctly"""

        self.assertEqual(encrypt(0, 'abcde'), 'abcde')
        self.assertEqual(encrypt(1, 'abcde'), 'bcdef')
        self.assertEqual(encrypt(2, 'abcde'), 'cdefg')

    def test_encrypt_type_error_int(self):
        """Encrypt method raises TypeError on bad input"""

        with self.assertRaises(TypeError):
            encrypt('0', 'abcde')

        with self.assertRaises(TypeError):
            encrypt(True, 'abcde')

        with self.assertRaises(TypeError):
            encrypt(4.2, 'abcde')

        with self.assertRaises(TypeError):
            encrypt([], 'abcde')

    def test_encrypt_type_error_int(self):
        """Encrypt method raises TypeError on bad input"""

        with self.assertRaises(TypeError):
            encrypt(2, 4)

        with self.assertRaises(TypeError):
            encrypt(2, 5.5)

        with self.assertRaises(TypeError):
            encrypt(2, True)

        with self.assertRaises(TypeError):
            encrypt(2, [])

    def test_decrypt(self):
        """Decrypt method works correctly"""

        self.assertEqual(decrypt(0, 'abcde'), 'abcde')
        self.assertEqual(decrypt(1, 'bcdef'), 'abcde')
        self.assertEqual(decrypt(2, 'cdefg'), 'abcde')

    def test_decrypt_type_error_int(self):
        """decrypt method raises TypeError on bad input"""

        with self.assertRaises(TypeError):
            decrypt('0', 'abcde')

        with self.assertRaises(TypeError):
            decrypt(True, 'abcde')

        with self.assertRaises(TypeError):
            decrypt(4.2, 'abcde')

        with self.assertRaises(TypeError):
            decrypt([], 'abcde')

    def test_decrypt_type_error_int(self):
        """decrypt method raises TypeError on bad input"""

        with self.assertRaises(TypeError):
            decrypt(2, 4)

        with self.assertRaises(TypeError):
            decrypt(2, 5.5)

        with self.assertRaises(TypeError):
            decrypt(2, True)

        with self.assertRaises(TypeError):
            decrypt(2, [])

    def test_get_cli_parameters(self):
        """cli parameters function working correctly"""
        cli_params = ['_', 5, 'test_text.txt', 'output.txt']
        num_steps, filename, output_file = get_cli_parameters(cli_params)
        
        self.assertEqual(num_steps, 5)
        self.assertEqual(filename, 'test_text.txt')
        self.assertEqual(output_file, 'output.txt')

    def test_get_cli_parameters_incomplete_parameters(self):
        """Raise index error if all parameters are not given"""
        cli_params = ['_', 5, 'test_text.txt']

        with self.assertRaises(IndexError):
            num_steps, filename, output_file = get_cli_parameters(cli_params)
    
    def test_get_cli_parameters_type_errors(self):
        """Raise value error if num_steps is not an int"""
        cli_params = ['_', 'error', 'test_text.txt', 'output.txt']

        with self.assertRaises(ValueError):
            num_steps, filename, output_file = get_cli_parameters(cli_params)
    
    def test_get_cli_parameters_empty_strings(self):
        """Raise value error if all parameters are not given"""
        cli_params = ['_', 5, '', '']

        with self.assertRaises(ValueError):
            num_steps, filename, output_file = get_cli_parameters(cli_params)

    def test_get_cli_parameters_input_file_exists(self):
        """Raise file not found error if filename doesn't exist"""

        cli_params = ['_', 5, 'not_exists.txt', 'output.txt']

        with self.assertRaises(FileNotFoundError):
            num_steps, filename, output_file = get_cli_parameters(cli_params)
        self.assertFalse(os.path.exists('not_exists.txt'))

    def test_test_file_exists(self):
        """test_txt file exists"""

        filename = "test_text.txt"
        self.assertTrue(os.path.exists(filename))

    def test_test_file_contents(self):
        """test_txt contents is abcde"""

        filename = "test_text.txt"
        with open(filename) as file:
            contents = file.read()
        
        self.assertEqual(contents, 'abcde')
    
    def test_encrypt_file_check_file_created(self):
        """File created with encrypt file"""

        os.system("python3 encrypt_file.py 2 test_text.txt test_encrypted_text.txt")
        
        self.assertTrue(os.path.exists("test_encrypted_text.txt"))

    def test_encrypt_file_bad_input(self):
        """Trigger exception to check if file was not created"""

        os.system("python3 encrypt_file.py 2 not_exists.txt test_encrypted_text.txt")
        
        self.assertFalse(os.path.exists("test_encrypted_text.txt"))

    def test_encrypt_file_contents(self):
        """Contents of output file is encrypted"""
        
        os.system("python3 encrypt_file.py 2 test_text.txt test_encrypted_text.txt")
        
        with open("test_encrypted_text.txt") as file:
            encrypted_content = file.read()

        self.assertEqual(encrypted_content, 'cdefg')
    

if __name__ == '__main__':
    unittest.main()
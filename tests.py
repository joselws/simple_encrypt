from encryption import encrypt, decrypt, get_cli_parameters
import os
import unittest


class TestEncryption(unittest.TestCase):
    """Tests for encryption module"""

    def tearDown(self):
        """Reset the test.txt file"""

        with open('test_text.txt', 'w') as file:
            file.write('abcde')


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
        cli_params = ['_', 5, 'test_text.txt']
        num_steps, filename = get_cli_parameters(cli_params)
        
        self.assertEqual(num_steps, 5)
        self.assertEqual(filename, 'test_text.txt')

    def test_get_cli_parameters_incomplete_parameters(self):
        """Raise index error if all parameters are not given"""
        cli_params = ['_', 5]

        with self.assertRaises(IndexError):
            num_steps, filename = get_cli_parameters(cli_params)
    
    def test_get_cli_parameters_type_errors(self):
        """Raise value error if num_steps is not an int"""
        cli_params = ['_', 'error', 'test_text.txt']

        with self.assertRaises(ValueError):
            num_steps, filename = get_cli_parameters(cli_params)
    
    def test_get_cli_parameters_empty_strings(self):
        """Raise value error if all parameters are not given"""
        cli_params = ['_', 5, '']

        with self.assertRaises(ValueError):
            num_steps, filename = get_cli_parameters(cli_params)

    def test_get_cli_parameters_input_file_exists(self):
        """Raise file not found error if filename doesn't exist"""

        cli_params = ['_', 5, 'not_exists.txt']

        with self.assertRaises(FileNotFoundError):
            num_steps, filename = get_cli_parameters(cli_params)
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
    
    def test_encrypt_file_contents(self):
        """Contents of output file is encrypted"""
        
        os.system("python3 encrypt_file.py 2 test_text.txt")
        
        with open("test_text.txt") as file:
            encrypted_content = file.read()

        self.assertEqual(encrypted_content, 'cdefg')
    
    def test_decrypt_file_contents(self):
        """Contents of output file is decrypted"""
        
        os.system("python3 encrypt_file.py 2 test_text.txt")
        os.system("python3 decrypt_file.py 2 test_text.txt")
         
        with open("test_text.txt") as file:
            decrypted_content = file.read()

        self.assertEqual(decrypted_content, 'abcde')
    

if __name__ == '__main__':
    unittest.main()
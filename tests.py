from cipher import cipher, get_cli_parameters
from exceptions import CipherError, CLIParamsError
import os
import unittest


class TestGetCLIParameters(unittest.TestCase):
    """Tests for get_cli_parameters function"""

    def test_correct_cli_params(self):
        """Function works correctly with minimum valid list elements"""

        args = ["encrypt", "10", "test_text.txt"]
        args2 = ["decrypt", "5", "test_text.txt"]

        self.assertEqual(get_cli_parameters(args), ("encrypt", 10, ["test_text.txt"]))
        self.assertEqual(get_cli_parameters(args2), ("decrypt", 5, ["test_text.txt"]))

    def test_invalid_action_type(self):
        """Action must always be 'encrypt' or 'decrypt'"""

        args = ["test", "10", "test_text.txt"]

        with self.assertRaises(CLIParamsError):
            get_cli_parameters(args)

    def test_invalid_cli_params_length(self):
        """Minimum cli parameters is 3'"""

        args = ["encrypt", "10",]
        args2 = []

        with self.assertRaises(CLIParamsError):
            get_cli_parameters(args)
        with self.assertRaises(CLIParamsError):
            get_cli_parameters(args2)

    def test_invalid_key_value(self):
        """Key parameter must be a positive number"""

        args = ["encrypt", "-10", "test_text.txt"]
        args2 = ["encrypt", "0", "test_text.txt"]

        with self.assertRaises(CLIParamsError):
            get_cli_parameters(args)
        with self.assertRaises(CLIParamsError):
            get_cli_parameters(args2)

    def test_invalid_key_type(self):
        """Key parameter must be a positive number"""

        args3 = ["encrypt", "hi", "test_text.txt"]

        with self.assertRaises(ValueError):
            get_cli_parameters(args3)

    def test_file_not_found(self):
        """Error raised when file not found"""
        
        args = ["encrypt", "10", "no_exists.txt"]

        with self.assertRaises(FileNotFoundError):
            get_cli_parameters(args)

    def test_multiple_files_working(self):
        """Function works with multiple files"""

        os.system('> test_text2.txt')
        os.system('> test_text3.txt')

        args = ["encrypt", "10", "test_text.txt", "test_text2.txt", "test_text3.txt"]
        self.assertEqual(get_cli_parameters(args), ("encrypt", 10, ["test_text.txt", "test_text2.txt", "test_text3.txt"]))

        os.remove("test_text2.txt")
        os.remove("test_text3.txt")

if __name__ == '__main__':
    unittest.main()
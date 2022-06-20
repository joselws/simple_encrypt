from encryption import encrypt, decrypt
import unittest


class TestEncryption(unittest.TestCase):
    """Tests for encryption module"""
    
    def test_encrypt(self):
        """Encrypt method works correctly"""

        self.assertEqual(encrypt(0, 'abcde'), 'abcde')
        self.assertEqual(encrypt(1, 'abcde'), 'bcdef')
        self.assertEqual(encrypt(2, 'abcde'), 'cdefg')

    def test_decrypt(self):
        """Decrypt method works correctly"""

        self.assertEqual(decrypt(0, 'abcde'), 'abcde')
        self.assertEqual(decrypt(1, 'bcdef'), 'abcde')
        self.assertEqual(decrypt(2, 'cdefg'), 'abcde')


if __name__ == '__main__':
    unittest.main()
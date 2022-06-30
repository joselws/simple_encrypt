# Simple Encryption

This is a simple Python encryption program that uses a pseudo Caesar Cipher method to encrypt and decrypt pieces of texts.

## REPL usage

You may use the encryption and decryption features by importing `encrypt` and `decrypt` from encryption.py like this.

```
>>> from encryption import encrypt, decrypt
```

Use `encrypt()` to encrypt a string given an integer "key". For example:

```
>>> encrypt(5, 'Hello World!')
'Mjqqt%\\twqi&'
```

Use `decrypt()` to decrypt a string given the same integer "key" used in `encrypt()`. For example:

```
>>> decrypt(5, 'Mjqqt%\\twqi&')
'Hello World!'
```

## CLI program usage

You may encrypt and decrypt files using the CLI.

### Encrypt files

Use the **encrypt_file.py** module to encrypt an existing text file. For example, the following command will encrypt the contents of the **credentials.txt** file using a "key" of 10:

```
python3 encrypt_file.py 10 credentials.txt
```

### Decrypt files

Use the **decrypt_file.py** module to decrypt an existing encrypted text file. For example, the following command will decrypt the contents of the **encrypted_credentials.txt** file using a "key" of 10:

```
python3 decrypt_file.py 10 encrypted_credentials.txt
```
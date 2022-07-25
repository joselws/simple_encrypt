# Pseudo Caesar Cipher

This is a simple Python encryption program that uses a pseudo Caesar Cipher method to encrypt and decrypt pieces of texts.

## REPL usage

You may use the cipher feature by importing `cipher` and from `cipher.py` like this:

```
>>> from cipher import cipher
```

Use `cipher()` to encrypt or decrypt a string given an integer "key". Encrypt will move each character the *key* steps forward and decrypt will move them backwards. For example:

```
>>> cipher("encrypt", 5, 'Hello World!')
'Mjqqt%\\twqi&'
```

```
>>> cipher("decrypt", 5, 'Mjqqt%\\twqi&')
'Hello World!'
```

## CLI program usage

You may encrypt and decrypt files using the CLI.

### Cipher files

Use the **cipher_file.py** module to encrypt/decrypt an existing text file. For example, the following command will encrypt the contents of the **credentials.txt** file using a "key" of 10:

```
python3 cipher_file.py encrypt 10 credentials.txt
```

You may also encrypt/decrypt multiple files in a single command by passing their names as arguments. For example:

```
python3 cipher_file.py encrypt 10 credentials.txt credentials2.txt credentials3.txt
```
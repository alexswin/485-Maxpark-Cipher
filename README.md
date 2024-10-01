# 485 Maxpark Cipher

This code will allow you to encrypt and decrypt text using the Maxpark Cipher (developed by Betty Rogers, Olivia Harrison, and Alex Swindler for MATH 485). The Maxpark Cipher is inspired by Rubik's Cubes. For further information, see the full cryptosystem document.

### Running the Script

```
$ python3 cipher.py
```

You may be prompted by your shell to install numpy and/or secrets.

```
$ pip install numpy secrets
```

### User Input

When you start the script, you will be prompted to enter the cipher keys. The setup key should be a string of letters of the alphabet. The rotation key should consist of some combination of the following, each separated by a space: U, U', D, D', F, F', B, B', L, L', R, R'. For example:
```
F' B R' R' F U U L U'
```

Next, you will be asked whether you wish to encrypt or decrypt. Upon selecting an option, you will be prompted for the plaintext or ciphertext.

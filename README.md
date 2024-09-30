# 485 Cipher Scrambler

This code will allow you to input a Cube and do Rubik's Cube-style transformations on it. For notation information, see the full cryptosystem document.

### Running the Script

```
$ python3 cipher.py
```

You may be prompted by your shell to install numpy.

```
$ pip install numpy
```

### User Input

When you start the script, you will be prompted to enter your matrix values. At this point, you should have already done the setup step with k<sub>s</sub>. If your k<sub>s</sub> was alphabetical (ex. ABCDEFGH), this is how you should input the values into the script:

```
Enter your 3x3x3 matrix (3 lines, 3 space-separated strings (ex. A B C) each, for each layer):
Bottom Layer (z=0):
G H I
D E F
A B C
Middle Layer (z=1):
O P Q
M _ N
J K L
Top Layer (z=2):
X Y Z
U V W
R S T
```

In this case, A corresponds to (0,0,0) and I corresponds to (2,2,0).

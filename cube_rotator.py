import numpy as np

def get_matrix(key_s_complete):
    matrix = []
    for i in range(3):
        layer = []
        for j in range(3):
            row = []
            for k in range(3):
                row.append(key_s_complete[9*i + 3*j + k])
            layer.insert(0,row)
        matrix.append(layer)
    return np.array(matrix)

def rotate_left(matrix, isClockwise):
    temp = matrix.copy()
    if isClockwise:
        # bottom layer
        matrix[0][0][0] = temp[0][2][0]
        matrix[0][1][0] = temp[1][2][0]
        matrix[0][2][0] = temp[2][2][0]
        
        # middle layer
        matrix[1][0][0] = temp[0][1][0]
        matrix[1][2][0] = temp[2][1][0]

        # top layer
        matrix[2][0][0] = temp[0][0][0]
        matrix[2][1][0] = temp[1][0][0]
        matrix[2][2][0] = temp[2][0][0]
    else:
        # bottom layer
        matrix[0][0][0] = temp[2][0][0]
        matrix[0][1][0] = temp[1][0][0]
        matrix[0][2][0] = temp[0][0][0]
        
        # middle layer
        matrix[1][0][0] = temp[2][1][0]
        matrix[1][2][0] = temp[0][1][0]

        # top layer
        matrix[2][0][0] = temp[2][2][0]
        matrix[2][1][0] = temp[1][2][0]
        matrix[2][2][0] = temp[0][2][0]


def rotate_right(matrix, isClockwise):
    temp = matrix.copy()
    if isClockwise:
        # bottom layer
        matrix[0][0][2] = temp[2][0][2]
        matrix[0][1][2] = temp[1][0][2]
        matrix[0][2][2] = temp[0][0][2]
        
        # middle layer
        matrix[1][0][2] = temp[2][1][2]
        matrix[1][2][2] = temp[0][1][2]

        # top layer
        matrix[2][0][2] = temp[2][2][2]
        matrix[2][1][2] = temp[1][2][2]
        matrix[2][2][2] = temp[0][2][2]
    else:
        # bottom layer
        matrix[0][0][2] = temp[0][2][2]
        matrix[0][1][2] = temp[1][2][2]
        matrix[0][2][2] = temp[2][2][2]
        
        # middle layer
        matrix[1][0][2] = temp[0][1][2]
        matrix[1][2][2] = temp[2][1][2]

        # top layer
        matrix[2][0][2] = temp[0][0][2]
        matrix[2][1][2] = temp[1][0][2]
        matrix[2][2][2] = temp[2][0][2]

# Function to rotate the front face
def rotate_front(matrix, isClockwise):
    if isClockwise:
        # Rotate the bottom rows across all layers in the clockwise direction
        temp = matrix.copy()
        # bottom layer
        matrix[0][2][0] = temp[0][2][2]
        matrix[0][2][1] = temp[1][2][2]
        matrix[0][2][2] = temp[2][2][2]
        # middle layer
        matrix[1][2][0] = temp[0][2][1]
        #matrix[1][2][1] stays the same
        matrix[1][2][2] = temp[2][2][1]
        # top layer
        matrix[2][2][0] = temp[0][2][0]
        matrix[2][2][1] = temp[1][2][0]
        matrix[2][2][2] = temp[2][2][0]
    else:
        # Rotate the bottom rows across all layers in the counterclockwise direction
        temp = matrix.copy()
        # bottom layer
        matrix[0][2][0] = temp[2][2][0]
        matrix[0][2][1] = temp[1][2][0]
        matrix[0][2][2] = temp[0][2][0]
        # middle layer
        matrix[1][2][0] = temp[2][2][1]
        #matrix[1][2][1] stays the same
        matrix[1][2][2] = temp[0][2][1]
        # top layer
        matrix[2][2][0] = temp[2][2][2]
        matrix[2][2][1] = temp[1][2][2]
        matrix[2][2][2] = temp[0][2][2]
    return matrix

# Function to rotate the back face
def rotate_back(matrix, isClockwise):
    temp = matrix.copy()
    if isClockwise:
        # Rotate the top rows across all layers in the clockwise direction
        # bottom layer
        matrix[0][0][0] = temp[2][0][0]
        matrix[0][0][1] = temp[1][0][0]
        matrix[0][0][2] = temp[0][0][0]
        # middle layer
        matrix[1][0][0] = temp[2][0][1]
        #matrix[1][0][1] stays the same
        matrix[1][0][2] = temp[0][0][1]
        # top layer
        matrix[2][0][0] = temp[2][0][2]
        matrix[2][0][1] = temp[1][0][2]
        matrix[2][0][2] = temp[0][0][2]
    else:
        # Rotate the top rows across all layers in the counterclockwise direction
        # bottom layer
        matrix[0][0][0] = temp[0][0][2]
        matrix[0][0][1] = temp[1][0][2]
        matrix[0][0][2] = temp[2][0][2]
        # middle layer
        matrix[1][0][0] = temp[0][0][1]
        #matrix[1][0][1] stays the same
        matrix[1][0][2] = temp[2][0][1]
        # top layer
        matrix[2][0][0] = temp[0][0][0]
        matrix[2][0][1] = temp[1][0][0]
        matrix[2][0][2] = temp[2][0][0]
    return matrix

def rotate_layer(matrix, layer_index, isClockwise: bool):    
    # Rotate layer
    if isClockwise:
        matrix[layer_index] = np.rot90(matrix[layer_index], k=-1)
    else:
        matrix[layer_index] = np.rot90(matrix[layer_index], k=1)
    return matrix

def scramble_cube(matrix, k_r):
    for choice in k_r:
        if choice == 'U':
            rotate_layer(matrix, 2, True)
        elif choice == 'U\'':
            rotate_layer(matrix, 2, False)
        elif choice == 'D':
            rotate_layer(matrix, 0, False)
        elif choice == 'D\'':
            rotate_layer(matrix, 0, True)
        elif choice == 'F':
            rotate_front(matrix, True)
        elif choice == 'F\'':
            rotate_front(matrix, False)
        elif choice == 'B':
            rotate_back(matrix, True)
        elif choice == 'B\'':
            rotate_back(matrix, False)
        elif choice == 'L':
            rotate_left(matrix, True)
        elif choice == 'L\'':
            rotate_left(matrix, False)    
        elif choice == 'R':
            rotate_right(matrix, True)
        elif choice == 'R\'':
            rotate_right(matrix, False)
        else:
            raise Exception("Error: k_r must be a vector containing ONLY \"U\", \"U'\", \"D\", \"D'\", \"F\", \"F'\", \"B\", \"B'\", \"L\", \"L'\", \"R\", \"R'\"")

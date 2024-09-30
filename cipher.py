import numpy as np

def get_matrix():
    layer_names = ["Bottom", "Middle", "Top"]
    print("Enter your 3x3x3 matrix (3 lines, 3 space-separated strings (ex. A B C) each, for each layer):")
    matrix = []
    for i in range(3):
        layer = []
        print(f"{layer_names[i]} Layer (z={i}):")
        for _ in range(3):
            row = list(map(str, input().split()))
            layer.append(row)
        matrix.append(layer)
    return np.array(matrix)

def display_matrix(matrix):
    layer_names = ["Bottom", "Middle", "Top"]
    for i in range(3):
        print(f"{layer_names[2-i]} Layer (z={2-i}):")
        print(matrix[2-i])

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

def main():
    matrix = get_matrix()
    
    while True:
        print("\nCurrent Matrix:")
        display_matrix(matrix)
        
        choice = input("\nEnter 'quit' to stop.\nThe move options are U, U', D, D', R, R', L, L', F, F', B, B'.\nEnter the move you'd like to make: ")
        if choice == 'quit':
            break

        if choice == 'U':
            print("Rotating up clockwise")
            rotate_layer(matrix, 2, True)
        elif choice == 'U\'':
            print("Rotating up counterclockwise")
            rotate_layer(matrix, 2, False)
        elif choice == 'D':
            print("Rotating down clockwise")
            rotate_layer(matrix, 0, False)
        elif choice == 'D\'':
            print("Rotating down counterclockwise")
            rotate_layer(matrix, 0, True)
        elif choice == 'F':
            print("Rotating front clockwise")
            rotate_front(matrix, True)
        elif choice == 'F\'':
            print("Rotating front counterclockwise")
            rotate_front(matrix, False)
        elif choice == 'B':
            print("Rotating back clockwise")
            rotate_back(matrix, True)
        elif choice == 'B\'':
            print("Rotating back counterclockwise")
            rotate_back(matrix, False)
        elif choice == 'L':
            print("Rotating left clockwise")
            rotate_left(matrix, True)
        elif choice == 'L\'':
            print("Rotating left counterclockwise")
            rotate_left(matrix, False)    
        elif choice == 'R':
            print("Rotating right clockwise")
            rotate_right(matrix, True)
        elif choice == 'R\'':
            print("Rotating right counterclockwise")
            rotate_right(matrix, False)
        else:
            break

    print("\nNew Matrix:")
    display_matrix(matrix)

if __name__ == "__main__":
    main()
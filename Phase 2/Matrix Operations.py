import numpy as np

def get_matrix():
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))
    print("Enter the entries row-wise:")
    entries = list(map(int, input().split()))
    return np.array(entries).reshape(rows, cols)

def add_matrices(a, b):
    return np.add(a, b)

def subtract_matrices(a, b):
    return np.subtract(a, b)

def multiply_matrices(a, b):
    return np.dot(a, b)

def transpose_matrix(a):
    return np.transpose(a)

if __name__ == "__main__":
    print("Matrix Operations using numpy")
    matrix1 = get_matrix()
    matrix2 = get_matrix()
    
    operation = input("Choose the operation (add/subtract/multiply/transpose): ").strip()
    
    if operation == "add":
        result = add_matrices(matrix1, matrix2)
    elif operation == "subtract":
        result = subtract_matrices(matrix1, matrix2)
    elif operation == "multiply":
        result = multiply_matrices(matrix1, matrix2)
    elif operation == "transpose":
        result = transpose_matrix(matrix1)
    else:
        print("Invalid operation")
        exit()
    
    print("Result:")
    print(result)

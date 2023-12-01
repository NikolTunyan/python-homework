import random

def generate_matrix(rows, cols):
    return [[random.randint(1, 20) for _ in range(cols)] for _ in range(rows)]

def generate_vector(elems):
    return [random.randint(1, 20) for _ in range(elems)]

def multiply_matrix_and_vector(matrix, vector):
    if len(matrix[0]) != len(vector):
        raise ValueError("The number of columns in the matrix should be equal to the number of elements in the vector")

    result = [sum(row[j] * vector[j] for j in range(len(vector))) for row in matrix]

    return result

def print_matrix(matrix):
    for row in matrix:
        print(row)

def write_to_file(filename, content):
    try:
        with open(filename, 'w') as txt_file:
            txt_file.write(f"{content}")
    except FileNotFoundError:
        print("Error: The new file could not be created.")

matrix = generate_matrix(4, 7)
vector1 = generate_vector(10)
vector2 = generate_vector(7)

print("The matrix:")
print_matrix(matrix)

print("Vector 1:")
print(vector1)

print("Vector 2:")
print(vector2)

result = multiply_matrix_and_vector(matrix, vector2)
print("Result: ")
print(result)

write_to_file("file.txt", result)

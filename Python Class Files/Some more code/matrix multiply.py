# Define two matrices
A = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

B = [[10, 11, 12],
     [13, 14, 15],
     [16, 17, 18]]

# Create a result matrix filled with zeros, dimensions should be same as input matrix
result = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]

# Perform matrix multiplication
for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(B)):
            result[i][j] += A[i][k] * B[k][j]

# Print the result
for r in result:
    print(r)

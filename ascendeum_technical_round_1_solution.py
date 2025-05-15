from typing import List
# To obtain the required coordinates to shape the array in spiral structure
def get_all_required_coordinates(rows, cols):
    top, bottom, left, right = 0, rows - 1, 0, cols - 1
    while top<=bottom and left<=right:
        # Traversing from top left -> top right
        for c in range(left, right + 1):
            yield top, c
        top += 1
        
        # Traversing fro top-right to bottom-right
        for r in range(top, bottom + 1):
            yield r, right
        right -= 1
        
        # Traversing from bottom-right to bottom-left
        if top<=bottom:
            for c in range(right, left - 1, -1):
                yield bottom, c
            bottom -= 1
        
        # Traversing from bottom-left to top-left
        if left<=right:
            for r in range(bottom, top - 1, -1):
                yield r, left
            left += 1
        
# To create the array
def arrange_array(matrix):
    rows, cols = len(matrix), len(matrix[0])
    # Tim Sort (Heap + Insertion)
    sorted_cols = sorted(val for row in matrix for val in row)
    n = len(matrix)
    output_matrix: List[List[int]] = [[0] * n for _ in range(n)]
    
    for (x, y), value in zip(get_all_required_coordinates(rows, cols), sorted_cols):
        output_matrix[x][y] = value
    
    return output_matrix
        
# Calling of functions
# src_matrix = [[1,2,3,4],
#             [5,6,7,8],
#             [9,10,11,12],
#             [13,14,15,16]]

n = int(input('Enter the length of the matrix for getting the ascending spiral patterned matrix!'))
count = 1
src_matrix: List[List[int]] = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        src_matrix[i][j] = count
        count += 1
        
output_matrix = arrange_array(src_matrix)
for row in output_matrix:
    print(row)
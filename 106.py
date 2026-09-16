rows = 3
n = int(input("Enter N (length): "))
matrix = [[0] * n for _ in range(rows)]
row = 0
going_down = True
for col in range(n):
    matrix[row][col] = 1
    if going_down:
        row += 1
        if row == rows:
            row = rows - 2
            going_down = False
    else:
        row -= 1
        if row < 0:
            row = 1
            going_down = True

for r in matrix:
    print(" ".join("*" if v else " " for v in r))

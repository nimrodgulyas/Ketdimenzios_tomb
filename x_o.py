tabla = [
    ['X', 'O', None],
    [None, 'X', 'O'],
    ['O', None, 'X']
]

for i in range(len(tabla)):
    for j in range(len(tabla[i])):
        if tabla[i][j] == None:
            print("_", end=" ")
        else:
            print(tabla[i][j], end=" ")
    print()

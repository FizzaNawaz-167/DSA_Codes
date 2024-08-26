P = [ [7, 5, 0, 0],
      [7, 0, 0, 2],
      [0, 3, 0, 0],
      [4, 0, 1, 0] ]

for k in range(4):
    for i, row in enumerate(P):
        for j, col in enumerate(row):
            # value1 = 99999 if P[i][j] == 0 else P[i][j]
            # value2 = 99999 if P[i][k] == 0 else P[i][k]
            # value3 = 99999 if P[k][j] == 0 else P[k][j]   

            # P[i][j] = min(value1, (value2 + value3))

            # print(f'P[{i}][{j}] , (P[{i}][{k}] + P[{k}][{j}])')
            print(f'{P[i][j]} , {P[i][k]} + {P[k][j]}')

    # print(f'A{k+1}: ____v1______v2______v3______v4')
    # for i, row in enumerate(P):
    #     print(f'v{i+1}', end=' | ')
    #     for j, col in enumerate(row):
    #         value = '~' if P[i][j] == 99999 else P[i][j]
    #         print(f'\t{value}', end='')
    #     print()
    print('\n')     
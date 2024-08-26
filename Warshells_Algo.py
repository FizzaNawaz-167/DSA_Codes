P = [ [0, 0, 0, 1],
      [1, 0, 1, 1],
      [1, 0, 0, 1],
      [0, 0, 1, 0] ]

for k in range(4):
    for i, row in enumerate(P):
        for j, col in enumerate(row):
            P[i][j] = P[i][j] or (P[i][k] and P[k][j])

    # print(f'A{k+1}:')
    print(f'A{k+1}: ____v1______v2______v3______v4')
    for i, row in enumerate(P):
        print(f'v{i+1}', end=' | ')
        for j, col in enumerate(row):
            print(f'\t{P[i][j]}', end='')
        print()
    print('\n')        
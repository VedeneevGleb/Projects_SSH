n = int(input())
result = {}
for i in range(n):
    game = input().split(';')
    if game[0] not in result.keys():
        result[game[0]] = [0, 0, 0, 0, 0]
    if game[2] not in result.keys():
        result[game[2]] = [0, 0, 0, 0, 0]
    result[game[0]][0] += 1
    result[game[2]][0] += 1
    if int(game[1]) > int(game[3]):
        result[game[0]][1] += 1
        result[game[2]][3] += 1
        result[game[0]][4] += 3
    elif int(game[1]) < int(game[3]):
        result[game[2]][1] += 1
        result[game[0]][3] += 1
        result[game[2]][4] += 3
    else:
        result[game[0]][2] += 1
        result[game[2]][2] += 1
        result[game[0]][4] += 1
        result[game[2]][4] += 1
for key, value in result.items():
    print(key + ':', end='')
    for it in value:
        print(it, end=' ')
    print()
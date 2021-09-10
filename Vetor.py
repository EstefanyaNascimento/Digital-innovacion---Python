x = float(input())

for i in range(0, 99):

    print('N[' + str(i) + '] = ' + str(format(x, '.4f')))

    x /= 2

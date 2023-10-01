n = int(input('Enter a odd number for pattern:- '))
if n % 2 != 0 and n >= 5:
    for i in range(n):
        if i == 0:
            print('* ' * ((n + 1) // 2), end='')
            print('  ' * (((n + 1) // 2) - 2), end='')
            print('*', end='')
        elif 0 < i < (n // 2):
            print('  ' * (n // 2), end='')
            print('* ', end='')
            print('  ' * (((n + 1) // 2) - 2), end='')
            print('*', end='')
        elif i == (n // 2):
            print('* ' * n, end='')

        elif (n // 2) < i < (n - 1):
            print('* ', end='')
            print('  ' * (((n + 1) // 2) - 2), end='')
            print('*', end='')
        elif i == (n - 1):
            print('* ', end='')
            print('  ' * (((n + 1) // 2) - 2), end='')
            print('* ' * ((n + 1) // 2), end='')
        print()
else:
    print('Only odd number and greater then 4 please!')

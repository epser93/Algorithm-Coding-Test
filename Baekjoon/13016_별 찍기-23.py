n = int(input())
half = (2 * n - 1) // 2

print('*' * n + ' ' * (2 * n - 3) + '*' * n)
for i in range(1, half):
    print(' ' * i + '*' + ' ' * (n - 2) + '*' + ' ' * ((2 * (n - 1) - 1) - 2 * i) + '*' + ' ' * (n - 2) + '*')

print(half * ' ' + '*' + ' ' * (n - 2) + '*' + ' ' * (n - 2) + '*')

for i in range(half + 1, 2 * n - 2):
    print(' ' * (2 * n - 1 - (i + 1)) + '*' + (n - 2) * ' ' + '*' + ' ' * (2 * i - (2 * n - 1)) + '*' + (n - 2) * ' ' + '*')

print('*' * n + ' ' * (2 * n - 3) + '*' * n)
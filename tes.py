def print_centered_triangle(n):
    for i in range(1, n + 1):
        print(' ' * (n - i) + '*' * (2 * i - 1))

n = 5
print_centered_triangle(n)

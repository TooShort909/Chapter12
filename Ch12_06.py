def sum_of_numbers(n):
    if n == 1:
        return 1
    else:
        return n + sum_of_numbers(n - 1)
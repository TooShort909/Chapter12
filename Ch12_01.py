def print_numbers(n):
    if n >= 1:  
        print_numbers(n - 1)
        print(n)  
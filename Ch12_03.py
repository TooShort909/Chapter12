def asterisks(n, current=1):
    if current > n:
        return
    print('*' * current)  
    asterisks(n, current + 1)
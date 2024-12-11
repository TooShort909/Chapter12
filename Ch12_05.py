def list_sum(lst):
    if not lst:  
        return 0
    return lst[0] + list_sum(lst[1:])
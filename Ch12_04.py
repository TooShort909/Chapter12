def find_max_in_list(numbers):
    if len(numbers) == 1:
        return numbers[0]
    max_of_rest = find_max_in_list(numbers[1:])
    return max(numbers[0], max_of_rest)
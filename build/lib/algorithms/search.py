def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high) / 2
        guess = list[mid]
        if item == guess:
            return mid
        elif guess > item:
            high = mid
        else:
            low = mid

    return None


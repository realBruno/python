def binary_search(list, item):

    low = 0
    high = len(numbers) - 1

    while low <= high:
        mid = (low + high)//2
        guess = list[mid]
        
        if guess == item:
            return mid
        
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
        return None

numbers = [i for i in range(1, 101)]

print(binary_search(numbers, 9))
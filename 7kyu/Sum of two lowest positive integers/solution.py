def sum_two_smallest_numbers(numbers):
    #your code here
    x = min(numbers)
    numbers.remove(min(numbers))
    return min(numbers)+x
    #print(min(numbers.remove(numbers.index(min(numbers)))))

def largest(numbers):
    if not numbers:
        return None, None, None
    largest =numbers[0]
    smallest = numbers[0]
    for no in numbers:
        if no>largest:
            largest = no
        if no<smallest:
            smallest =no
    return largest, smallest
numbers= [1,2,3,4,5,6,7,8]
largest, smallest = largest(numbers)
print(f"largest: {largest}, smallest: {smallest}")
    
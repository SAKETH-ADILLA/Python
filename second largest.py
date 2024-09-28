def second_largest(numbers):
    if len(numbers)<2:
        return None
    first = second = float('-inf')
    for no in numbers:
        if no>first:
            second = first
            first = no
        elif first > no > second:
            second = no
    return second  if second != float('-inf') else None

numbers = [34,39,32,454]
result = second_largest(numbers)
print(f"The second largest element is: {result}")
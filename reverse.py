def reverse(lst):
    start = 0
    end = len(lst) -1
    while start < end:
        lst [start], lst[end] = lst[end], lst[start]
        start +=1
        end -= 1
    return lst
input = [1,2,3,4,5,6]
reversed_no = reverse(input)
print(reversed_no)
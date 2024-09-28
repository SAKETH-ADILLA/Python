def calc(number):
    if not number:
        return None, None, None
    total = sum(number)
    count = len(number)
    average = total/count
    return total, count, average
number = [10,20,30,40,50]
total,count,average = calc(number)
print(f"Total: {total}, count: {count}, Average: {average}")
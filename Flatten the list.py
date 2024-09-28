def flatten_list(nested_list):
    flat_list= []
    for sublist in nested_list:
        flat_list.extend(sublist)
    return flat_list
input = [[1,2,3],[4,5,6],[7,8,9]]
flattend = flatten_list(input)
print(f"The flattened list is: {flattend}")

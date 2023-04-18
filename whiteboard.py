# Create a function name all_non_consecutive

# E.g., if we have an array [1,2,3,4,6,7,8,15,16] then 6 and 15 are non-consecutive.

# You should return the results as an array of objects with two values i: <the index of the non-consecutive number> and n: <the non-consecutive number>.

# E.g., for the above array the result should be:

# [
#   {'i': 4, 'n': 6},
#   {'i': 7, 'n': 15}
# ]
# If the whole array is consecutive or has one element then return an empty array.

# The array elements will all be numbers. The numbers will also all be unique and in ascending order. The numbers could be positive and/or negetive and the gap could be larger than one.

def anc(list):
    output = []
    for i in range(len(list) - 1):
        if list[i+1] - list[i] != 1:
            output.append({'i': i + 1, 'n:': list[i + 1]})
    return output


print(anc([1, 2, 3, 4, 6, 7, 8, 15, 16]))


def find_cons(alist):
    return [{'i': i, 'n': n} for i, n in enumerate(alist[1:], start=1) if n != alist[i-1]+1]


print(find_cons([1, 2, 3, 4, 6, 7, 8, 15, 16]))

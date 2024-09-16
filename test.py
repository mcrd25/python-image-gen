def second_min(arr):
    if len(arr) < 2:
        return None
    unique_elements = list(set(arr))
    unique_elements.sort()
    return unique_elements[1] if len(unique_elements) >= 2 else None

# Example usage
arr = [4, 3, 1, 2, 5, 1]
print(second_min(arr))

#non repeating
def first_non_repeating(arr):
    frequency = {}
    for num in arr:
        frequency[num] = frequency.get(num, 0) + 1
    for num in arr:
        if frequency[num] == 1:
            return num
    return None

# Example usage
arr = [4, 5, 7, 1, 2, 1, 4, 5]
print(first_non_repeating(arr))

# merge two sorted arrays

def merge_sorted(arr1, arr2):
    return sorted(arr1 + arr2)

# Example usage
arr1 = [1, 3, 5]
arr2 = [2, 4, 6]
print(merge_sorted(arr1, arr2))

# Rearrange positive and negative values in an array
def rearrange(arr):
    pos = [x for x in arr if x >= 0]
    neg = [x for x in arr if x < 0]
    return neg + pos

# Example usage
arr = [1, -2, 3, -4, 5, -6]
print(rearrange(arr))

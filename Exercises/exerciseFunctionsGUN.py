#Function to find the highest even number from a list.

def highest_even(li) -> int:

    current_highest = 0

    for item in li:
        if item % 2 == 0 and item >= current_highest:
            current_highest = item

    return current_highest

print(highest_even([10,4,5,6,3,7,11]))
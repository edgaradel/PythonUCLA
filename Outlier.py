def find_outlier(integers):
    count_even = 0
    count_odd = 0
    for i in integers[0:3]: #check if at least 2 of the first three elements in the string are even or odd.
        if i % 2 == 0:
            count_even += 1
        else:
            count_odd += 1
    if count_even >= 2:  # if at least 2 of the elements are even, find the odd number in the list
        for i in integers:
            if i % 2 != 0:
                return i          
    else:
         for i in integers:
                if i % 2 == 0:
                    return i

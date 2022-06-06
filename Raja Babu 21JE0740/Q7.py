def max_freq(lst):
    return max(set(lst), key=lst.count)


list1 = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5]
print(max_freq(list1))

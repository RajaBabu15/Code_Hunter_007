def dup(lst):
    for i in range(len(lst)):
        k = i + 1
        for j in range(k, len(lst)):
            if lst[i] == lst[j]:
                return lst[i]
    return "None"


list1 = [1, 1, 0, 4, 6, 9, 4]
print(list1, " contain ", dup(list1), " as duplicate element")

def alter(lst, params):
    if params == "asc":
        lst = lst.sort()
    elif params == "desc":
        lst = lst.sort(reverse=True)
    elif params == "None":
        lst = lst


list1 = [2, 5, 8, 1]
print("List1", list1)
alter(list1, params="asc")
print("List1 Ascending", list1)

list2 = [4, 9, 6, 3]
print("List2", list2)
alter(list2, params="desc")
print("List2 Descending", list2)

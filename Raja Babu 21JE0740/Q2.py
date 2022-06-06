def hide(num):
    str_arr = []
    for i, n in enumerate(num):
        if i >= len(num)-4:
            n = '*'
        str_arr.append(n)
    return "".join(str_arr)


num = 4444444444444444
print(hide(str(num)))

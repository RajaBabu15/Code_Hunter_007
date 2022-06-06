def sum(strng):
    s = 0
    for ch in strng:
        if ch.isnumeric():
            s += int(ch)
    return s


print("h20 15 wa73r\t", sum("h20 15 wa73r"))

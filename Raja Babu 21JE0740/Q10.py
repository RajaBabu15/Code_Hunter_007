def swap(a, b):
    a = a ^ b
    b = a ^ b
    a = a ^ b
    return a, b


(a, b) = (1, 2)
print("Before Swapping : a = ", a, " b  = ", b)
(a, b) = swap(a, b)
print("After Swapping : a = ", a, " b = ", b)

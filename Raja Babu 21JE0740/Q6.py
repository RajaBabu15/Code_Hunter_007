from pickle import TRUE


def prime(n):
    prime_no = []
    for i in range(2, n):
        f = False
        for j in range(2, i):
            if i % j == 0:
                f = True
                break
        if not f:
            prime_no.append(i)
    return prime_no


print(prime(100))

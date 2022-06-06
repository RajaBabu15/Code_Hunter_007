def operate(a, op, b):
    if op == '+':
        return a+b
    elif op == '-':
        return a-b
    elif op == '/':
        return a/b
    elif op == '.':
        return a*b
    else:
        return "Unindetified Operator"


n1 = int(input("n1 : "))
operator = input("operator(+,-,.,/) : ")
n2 = int(input("n2 : "))
print(operate(n1, operator, n2))

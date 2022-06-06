def double_IT(inp):
    op = []
    for i, ch in enumerate(inp):
        op.append(ch)
        op.append(ch)
    return "".join(op)


params = "abc123"
print(double_IT(params))

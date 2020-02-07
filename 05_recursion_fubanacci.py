def fun_seq(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fun_seq(n-1)+fun_seq(n-2)
print(fun_seq(11))
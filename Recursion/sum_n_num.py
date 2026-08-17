def sum_n_num(n):
    if n<1:
        return 0

    return n + sum_n_num(n-1)

x = sum_n_num(5)
print(x)
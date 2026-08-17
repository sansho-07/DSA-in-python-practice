def Power(x,n):
    if n!=0:
        return x * Power(x,n-1)
    else:
        return 1

x = float(input("Enter the base number: "))
n = int(input("Enter the power number: "))
calc_power = Power(x,n)
print(f'Power of a number is : {calc_power}')
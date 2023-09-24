def fact(n):
    if n == 0:
        return 1
    else:
        return n*(fact(n-1))


def comb(n,r):
    return fact(n)/(fact(r)*(fact(n-r)))


n1 = int(input("enter a no: "))
n2 = int(input("Enter a no: "))
print(comb(n1,n2))
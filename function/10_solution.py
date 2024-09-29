num =  int(input("please enter the number :"))

def fact(n):
    if(n==0):
        return 1
    else:
        a = n*(fact(n-1))
    return a

print(fact(num))
import math

n=int(input("Enter a number n: "))
m=n+1

def prime_check(n):
    if n<2:
        return False
    elif n==2:
        return True
    elif n%2==0:
        return False
    else:
        for i in range(3,int(math.sqrt(n))+1,2):
            if n%i==0: return False
    return True

while not prime_check(m):
    m=m+1

print("The first prime number larger than n is: ",m)
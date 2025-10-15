def isPrime(n):
    if(n ==1 or n == 0):
        return False
    
    for i in range(2,n-1):
        if(n%i == 0):
            return False
    return True

N = 100
counter = 0

for i in range(N):
    if(isPrime(i)):
        print(i)
        counter = counter + 1

print("\n" + str(counter) + " numeri primi")

print(isPrime(5))

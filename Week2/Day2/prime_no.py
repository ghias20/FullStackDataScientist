def prime_numbers(n):
    for num in range(2,n+1):
        is_prime=True
        for i in range(2,num):
            if num%i==0:
                return False
    return True
n=int(input("Enter a number to check if it is prime number: "))
print(prime_numbers(n))
def prime_numbers(n):
    primes=[]
    for num in range(2,n+1):
        is_prime=True
        for i in range(2,num):
            if num%i==0:
                is_prime=False
                break
        if is_prime:
            primes.append(num)
    return primes
n=int(input("Enter a number to generate prime numbers: "))
print(prime_numbers(n))
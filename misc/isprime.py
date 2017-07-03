def isprime(n):
    print('Is {} a prime number?'.format(n))

    if n == 1:
        print('{} is a special case'.format(n))
    for x in range(2, n):
        if n % x == 0:
            print('{} equals {} x {}\n'.format(n, x, n // x))
            print('{} is NOT a prime number'.format(n))
            return False
    else:
        print('{} is a prime number\n'.format(n))
        return True

for n in range (1, 50):
    isprime(n)
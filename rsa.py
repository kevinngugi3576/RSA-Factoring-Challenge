import sys

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def factorize(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            if is_prime(i) and is_prime(n//i):
                return (i, n//i)
    return None

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: rsa_factor <number>")
        sys.exit(1)

    n = int(sys.argv[1])

    factors = factorize(n)
    if factors:
        p, q = factors
        print(f"{n}={p}*{q}")
    else:
        print(f"{n} is prime.")


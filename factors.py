import sys

def factorize(n):
    factors = []
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            factors.append((i, n//i))
    return factors

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: factors <file>")
        sys.exit(1)

    filename = sys.argv[1]

    with open(filename, "r") as f:
        for line in f:
            n = int(line.strip())
            factors = factorize(n)
            for p, q in factors:
                print(f"{n}={p}*{q}")


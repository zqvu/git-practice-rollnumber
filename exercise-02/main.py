def factorial(n):
    if n < 0:
        raise ValueError("Number must be non-negative.")

    result = 1

    for i in range(1, n + 1):
        result *= i

    return result


def main():
    try:
        n = int(input("Enter a non-negative integer: "))
        print("Factorial:", factorial(n))
    except ValueError:
        print("Error: Enter a valid non-negative integer.")


if __name__ == "__main__":
    main()

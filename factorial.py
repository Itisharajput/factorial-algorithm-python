def factorial_iterative(n: int) -> int:
    """
    Calculate factorial of a number using iteration.

    Args:
        n (int): Non-negative integer

    Returns:
        int: Factorial of n

    Raises:
        ValueError: If n is negative
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")

    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def factorial_recursive(n: int) -> int:
    """
    Calculate factorial of a number using recursion.

    Args:
        n (int): Non-negative integer

    Returns:
        int: Factorial of n

    Raises:
        ValueError: If n is negative
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")

    if n == 0 or n == 1:
        return 1

    return n * factorial_recursive(n - 1)


if __name__ == "__main__":
    num = 5

    print(f"Iterative Factorial of {num}: {factorial_iterative(num)}")
    print(f"Recursive Factorial of {num}: {factorial_recursive(num)}")

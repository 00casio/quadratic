import math

def solve(a, b, c):
    """Solve a quadratic equation ax^2 + bx + c = 0"""
    if a == 0:
        raise ValueError("Coefficient 'a' cannot be 0")
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return "No real roots"
    elif discriminant == 0:
        x = -b / (2*a)
        return x
    else:
        x1 = (-b + math.sqrt(discriminant)) / (2*a)
        x2 = (-b - math.sqrt(discriminant)) / (2*a)
        return x1, x2

if __name__ == '__main__':
    import sys
    if len(sys.argv) != 4:
        print("Usage: solve_quadratic a b c")
    else:
        a, b, c = map(float, sys.argv[1:])
        result = solve(a, b, c)
        print(f"The roots are: {result}")

from utils import add, multiply, sqrt


def main():
    result = multiply(80.5, 33)
    print(f"The result of multiplication is {result}")
    
    print("You are on feature a Branch ")
    a = 10
    b = 50
    result = add(a, b)
    print(f"The result of the addition is {result}")


    n = 144
    result = sqrt(n)
    print(f"The square root of {n} equals {result}")

main()
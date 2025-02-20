import math

def add(a, b):
    """
    Adds two numbers
    """
    res = a + b
    return res

def multiply(a, b):
    """
    Multiplies two numbers
    """
    res = a * b 
    return res

def sqrt(a):
    """
    Calculates square root of a using built-in math library
    """
    res = math.sqrt(a)
    return res
    

if __name__ == "__main__":
    print("You are into utils.py")
    result = add(10, 20)
    print(result)
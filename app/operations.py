from .exceptions import OperationError

def add(a,b): return a+b
def subtract(a,b): return a-b
def multiply(a,b): return a*b
def divide(a,b):
    if b == 0: raise OperationError("Division by zero.")
    return a/b

def power(a,b): return a**b
def root(a,b):
    if b == 0: raise OperationError("Zeroth root undefined.")
    if a < 0 and int(b)%2==0: raise OperationError("Even root of negative.")
    return a**(1.0/b)
def modulus(a,b):
    if b == 0: raise OperationError("Modulus by zero.")
    return a % b
def int_divide(a,b):
    if b == 0: raise OperationError("Integer division by zero.")
    return int(a//b)
def percent(a,b):
    if b == 0: raise OperationError("Percent with zero denominator.")
    return (a/b)*100.0
def abs_diff(a,b): return abs(a-b)

def make_operation_table():
    return {
        "add": add, "subtract": subtract, "multiply": multiply, "divide": divide,
        "power": power, "root": root, "modulus": modulus, "int_divide": int_divide,
        "percent": percent, "abs_diff": abs_diff
    }

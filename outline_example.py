from types import FunctionType

# operations functions
def multiply(a:float, b:float) -> float:
    pass
def divide(numerator:float, denominator:float) -> float:
    pass
def add(a:float, b:float) -> float:
    pass
def subtract(a:float, b:float) -> float:
    pass

# read from user which operation he wants to do, returns corresponding function, or null
def read_operation() -> FunctionType:
    pass
# reads 2 floats
def read_values() -> tuple[float]:
    pass
# returns result of doing operation on given values
def perform_operation(a:float, b:float, operation:FunctionType) -> float:
    pass


# intro, hello

while True:
    # repeat until no operation is chosen
    operation = read_operation()
    if not operation: break
    a, b = read_values()
    result = perform_operation(a,b,operation)
    print(result)

# outro bye
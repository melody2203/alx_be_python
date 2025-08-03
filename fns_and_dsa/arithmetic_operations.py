def perform_operation(num1: float, num2: float,operation: str):
    match operation:
        case "add":
            result = num1 + num2
        case "subtract":
            result = num1 - num2
        case "multiply":
            result = num1 * num2
        case "divide":
            if num2 == 0:
                return None
            else:
                result = num1 / num2
        case _:
            return None
    return result
result = perform_operation(12.0,3.0,"add")
if result is None:
    print("Operation failed")
else:
    print("Result:", result)

   
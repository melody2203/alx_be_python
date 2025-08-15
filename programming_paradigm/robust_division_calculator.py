def safe_divide(numerator, denominator):
    try:
        numerator = float(numerator)
        denominator = float(denominator)
        return numerator / denominator
    except ZeroDivisionError:
        print("Denominator can't be zero. Please enter a non-zero number.")
    except ValueError:
       print("Invalid input. Please enter only a numeric value")
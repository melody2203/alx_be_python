class Calculator:
    # Class attribute
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """Static method: performs addition, no access to class/instance"""
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """Class method: can access class-level attributes"""
        print(f"Calculation type: {cls.calculation_type}")
        return a * b

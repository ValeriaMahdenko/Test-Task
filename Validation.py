class Validation:
    @staticmethod
    def validate_string(func):
        def stringWrapper(self, value):
            if any(map(str.isdigit, value)):
                raise ValueError("No integers in string!")
            return func(self, value)
        return stringWrapper

    @staticmethod
    def validate_number(func):
        def numberWrapper(self, value):
            try:
                value = int(value)
            except ValueError:
                raise ValueError("No letters/characters in number!")
            if int(value) < 0:
                raise ValueError("Number must be > 0")
            return func(self, value)
        return numberWrapper
 

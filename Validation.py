aclass Validation:
        @staticmethod
            def validate_string(func):
                        def stringWrapper(self, value):
                                        if any(map(str.isdigit, value)):
                                                            raise ValueError("No integers in string!")
                                                                    return func(self, value)
                                                                        return stringWrapper


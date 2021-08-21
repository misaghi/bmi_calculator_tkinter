class Arithmetic:

    def __init__(self, weight, height, mode):
        super().__init__()

        self.height = height
        self.weight = weight
        self.mode = mode
        self.__bmi = 0

    @property
    def bmi(self):
        try:
            self.__bmi = (self.weight) / pow(self.height, 2)
        except ZeroDivisionError:
            return False
        
        if self.mode == 'US':
            self.__bmi *= 703

        return round(self.__bmi, 2)
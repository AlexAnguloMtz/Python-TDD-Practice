class Assert:

    @staticmethod
    def is_positive(number):
        if (number <= 0):
            raise Exception('Expected positive number, was: ' + str(number))
class Assert:

    @staticmethod
    def is_number(tested):
        if (not (isinstance(tested, float) or isinstance(tested, int))):
            raise TypeError(f'Expected a number, was a {type(tested).__name__}')

    @staticmethod
    def is_positive(tested):
        Assert.is_number(tested)
        if (tested <= 0):
            raise ValueError(f'Expected positive number, was: {str(tested)}')
from Assert import Assert

class BodyMassIndex:

    @staticmethod
    def calculate(weight_kg, height_meters):
        Assert.is_positive(weight_kg)
        Assert.is_positive(height_meters)
        return (weight_kg / pow(height_meters, 2))
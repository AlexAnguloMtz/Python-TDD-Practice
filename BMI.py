class BMI():

    @staticmethod
    def calculate(weight_kg, height_meters):
        return (weight_kg / pow(height_meters, 2))
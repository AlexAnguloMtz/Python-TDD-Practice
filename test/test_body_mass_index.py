import unittest
from models import BodyMassIndex

class BodyMassIndexTest(unittest.TestCase):
    
    def test_should_calculate_BMI_correctly(self):
        weight_kg = 100
        height_meters = 2
        calculated_body_mass_index = BodyMassIndex.calculate(weight_kg, height_meters)
        self.assertEqual(25, calculated_body_mass_index)

    def test_should_raise_value_error_for_negative_numbers(self):
        self.assertRaises(ValueError, lambda: BodyMassIndex.calculate(-100, -25))
    
    def test_should_raise_type_error_for_non_numeric_inputs(self):
        self.assertRaises(TypeError, lambda: BodyMassIndex.calculate([], []))
        self.assertRaises(TypeError, lambda: BodyMassIndex.calculate({}, {}))
        self.assertRaises(TypeError, lambda: BodyMassIndex.calculate('string', 'string'))
        
if __name__ == '__main__':
    unittest.main()
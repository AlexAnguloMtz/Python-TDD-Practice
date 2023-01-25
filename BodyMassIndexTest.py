import unittest
from BodyMassIndex import BodyMassIndex

class BodyMassIndexTest(unittest.TestCase):
    
    def test_should_calculate_BMI_correctly(self):
        weight_kg = 100
        height_meters = 2
        calculated_body_mass_index = BodyMassIndex.calculate(weight_kg, height_meters)
        self.assertEqual(25, calculated_body_mass_index)
        
if __name__ == '__main__':
    unittest.main()
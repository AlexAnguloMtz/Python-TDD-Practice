"""
 Instructions: 
 1) Ask the user for their weight in kg
 2) Ask the user for their height in meters
 3) Calculate and show the BMI (Body Mass Index) with 2 decimal positions
 """
from BodyMassIndex import BodyMassIndex

def ask_float(prompt_message):
    return float(input(prompt_message))

def main():
    weight_kg = ask_float('Enter your weight in kg: ')
    height_meters = ask_float('Enter your height in meters: ')
    body_mass_index = BodyMassIndex.calculate(weight_kg, height_meters)
    print(f'Your body mass index is: {body_mass_index:.2f}')

main()
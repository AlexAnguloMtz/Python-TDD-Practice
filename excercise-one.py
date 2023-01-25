"""
 Instructions: 
 1) Ask the user for their weight in kg
 2) Ask the user for their height in meters
 3) Calculate and show the BMI (Body Mass Index) with 2 decimal positions
 """

def ask_float(prompt_message):
    return float(input(prompt_message))

def calculate_BMI(weight_kg, height_meters):
    return (weight_kg / pow(height_meters, 2))

def main():
    weight_kg = ask_float('Enter your weight in kg: ')
    height_meters = ask_float('Enter your height in meters: ')
    print(f'Your BMI is: {calculate_BMI(weight_kg, height_meters):.2f}')

main()
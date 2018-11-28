"""
Question 2
Body Mass Index
"""

print('BMI test')

print('Enter your height in feet and inchs: ')
height_feet = int(input('Feet: '))
height_inches = float(input('Inches: '))

weight = float(input('Enter your weight in pounds: '))

inches = (height_feet * 12) + height_inches

bmi = weight * (703/(inches**2))

if bmi < 18.5:
    print('Your BMI is %.1f and your are Underweight' % bmi)
elif bmi > 18.5 and bmi < 24.9:
    print('Your BMI is %.1f and your are normal weight' % bmi)
elif bmi > 25.0 and bmi < 29.9:
    print('Your BMI is %.1f and your are Overweight' % bmi)
else:
    print('Your BMI is %.1f and your are Obese' % bmi)
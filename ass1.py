"""
Question 1
Convert Latitude/Longitude to Decimal
"""

print('This will convert Latitude/Longitude to Decimal')

deg = float(input('Enter the degrees: '))

min = float(input('Enter the minutes: '))

sec = float(input('Enter the seconds: '))

decimal = deg + min/60.0 + sec/3600.0

print('The decimal is equal to %.4f' % decimal)


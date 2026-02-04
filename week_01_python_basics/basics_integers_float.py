# Basics of Integer and Float Operations in Python
# Integers are whole numbers (positive, negative, or zero) without a decimal point.
# Floats are numbers that contain a decimal point.
# Python supports various arithmetic operations on integers and floats.

# ============================================================================
# Basic Arithmetic Operations:
# Addition: +
# Subtraction: -    
# Multiplication: *
# Division: /
# Floor Division: //
# Modulus: %
# Exponentiation: **

# ============================================================================
# INDEX - Topics Covered in This File
# ============================================================================
# 1. Integer and Float Attributes and Methods (dir, help)
# 2. Basic Arithmetic Operations (+, -, *, /, //, %, **)
# 3. Type Conversion/Casting (int(), float())
# 4. Rounding Numbers (round())
# 5. Absolute Value (abs())
# 6. Comparison Operators (==, !=, >, <, >=, <=)
# ============================================================================

from pprint import pprint
# ============================================================================
# 1. INTEGER AND FLOAT ATTRIBUTES AND METHODS
# ============================================================================
print("\n" + "="*80)
print("1. INTEGER AND FLOAT ATTRIBUTES AND METHODS")
print("="*80)
pprint(dir(int))  # This will print all the attributes and methods available for integer objects.
pprint(help(int))  # This will print the help documentation for integer objects.
pprint(dir(float))  # This will print all the attributes and methods available for float objects.
pprint(help(float))  # This will print the help documentation for float objects.

# ============================================================================
# 2. BASIC ARITHMETIC OPERATIONS
# ============================================================================
print("\n" + "="*80)
print("2. BASIC ARITHMETIC OPERATIONS")
print("="*80)
a = 10
b = 3
print("Addition (a + b):", a + b)               # Output: 13
print("Subtraction (a - b):", a - b)            # Output: 7
print("Multiplication (a * b):", a * b)         # Output: 30
print("Division (a / b):", a / b)               # Output: 3.3333...
print("Floor Division (a // b):", a // b)       # Output: 3
print("Modulus (a % b):", a % b)               # Output: 1
print("Exponentiation (a ** b):", a ** b)       # Output: 1000

# ============================================================================
# 3. TYPE CONVERSION/CASTING
# ============================================================================
print("\n" + "="*80)
print("3. TYPE CONVERSION/CASTING")
print("="*80)
int_value = 5
float_value = 3.7
string_value = "10"
converted_to_float = float(int_value)
converted_to_int = int(float_value)
converted_to_int_from_string = int(string_value)
print("Convert integer to float:", converted_to_float)                     # Output: 5.0
print("Convert float to integer:", converted_to_int)                       # Output: 3
print("Convert string to integer:", converted_to_int_from_string)          # Output: 10

# ============================================================================
# 4. ROUNDING NUMBERS
# ============================================================================
print("\n" + "="*80)
print("4. ROUNDING NUMBERS")
print("="*80)
num = 5.6789
rounded_num = round(num, 2)
print("Round number to 2 decimal places:", rounded_num)                    # Output: 5.68

# ============================================================================
# 5. ABSOLUTE VALUE
# ============================================================================
print("\n" + "="*80)
print("5. ABSOLUTE VALUE")
print("="*80)
negative_num = -10
absolute_value = abs(negative_num)
print("Absolute value of -10:", absolute_value)                             # Output: 10

# ============================================================================
# 6. COMPARISON OPERATORS
# ============================================================================
print("\n" + "="*80)
print("6. COMPARISON OPERATORS")
print("="*80)
x = 10
y = 20
print("x == y:", x == y)           # Output: False
print("x != y:", x != y)           # Output: True
print("x > y:", x > y)             # Output: False
print("x < y:", x < y)             # Output: True
print("x >= y:", x >= y)           # Output: False
print("x <= y:", x <= y)           # Output: True

# End of basics_integers_float.py
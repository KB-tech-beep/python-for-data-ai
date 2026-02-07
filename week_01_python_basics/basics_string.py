# Basics of String Manipulation in Python
# A string is a sequence of characters enclosed in single quotes (' '), double quotes (" "), or triple quotes (''' ''' or """ """).
# Strings are immutable, meaning they cannot be changed after they are created.
# Strings can be manipulated using various built-in methods and operations.

# ============================================================================
# INDEX - Topics Covered in This File
# ============================================================================
# 1. String Attributes and Methods (dir, help)
# 2. Length of the String (len())
# 3. Slicing the String (indexing and ranges)
# 4. Changing Case (.upper(), .lower())
# 5. Counting Occurrences (.count())
# 6. Finding a Substring (.find())
# 7. Replacing a Substring (.replace())
# 8. String Concatenation AND INTERPOLATION (+, .format(), f-strings, .join())
# ============================================================================

from pprint import pprint
# ==========================================================================
# 1. STRING ATTRIBUTES AND METHODS
# ==========================================================================
print('\n' + '='*80)
print('1. STRING ATTRIBUTES AND METHODS')
print('='*80)
pprint(dir(str))  # This will print all the attributes and methods available for string objects.
pprint(help(str))  # This will print the help documentation for string objects.
pprint(help(str.upper))  # This will print the help documentation for the upper() method of string objects.

message = 'Hello, World!'

# ==========================================================================
# 2. LENGTH OF THE STRING
# ==========================================================================
print('\n' + '='*80)
print('2. LENGTH OF THE STRING')
print('='*80)
# len() function is a build-in function in Python that returns the number of items in an object, can be used with many data types(strings, lists, tuples, etc). When used with a string, it returns the number of characters in the string, including spaces and punctuation.
length = len(message)
print('Print the length of message string:', length)  # Output: 13

# ==========================================================================
# 3. SLICING THE STRING
# ==========================================================================
print('\n' + '='*80)
print('3. SLICING THE STRING')
print('='*80)
# Slicing is a way to extract a portion of a string by specifying a start and end index. The syntax is string[start:end], where 'start' is the index to begin the slice (inclusive) and 'end' is the index to end the slice (exclusive). Slicing is just part of Python's grammar, not a function.
first_five = message[0:5]
print('Print the first five characters of message string:', first_five)  # Output: Hello
first_five_without_start = message[:5]
print('Print the first five characters of message string without specifying start index:', first_five_without_start)  # Output: Hello
last_six = message[-6:]
print('Print the last six characters of message string:', last_six)  # Output: World!
last_six_without_last = message[6:]
print('Print the last six characters of message string without end index:', last_six_without_last)  # Output: World!

# ==========================================================================
# 4. CHANGING CASE
# ==========================================================================
print('\n' + '='*80)
print('4. CHANGING CASE')
print('='*80)
# Strings in Python have built-in methods to change their case. The .upper() method converts all characters in the string to uppercase, while the .lower() method converts all characters to lowercase.
upper_message = message.upper()
print('Print the message string in uppercase:', upper_message)  # Output: HELLO, WORLD!
lower_message = message.lower()
print('Print the message string in lowercase:', lower_message)  # Output: hello, world!

# ==========================================================================
# 5. COUNTING OCCURRENCES
# ==========================================================================
print('\n' + '='*80)
print('5. COUNTING OCCURRENCES')
print('='*80)
# The .count() method returns the number of occurrences of a substring in the string. It takes the substring as an argument.
count_l = message.count('l')
print('Print the number of occurrences of \'l\' in message string:', count_l)  # Output: 3
count_o = message.count('o')
print('Print the number of occurrences of \'o\' in message string:', count_o)  # Output: 2

# ==========================================================================
# 6. FINDING A SUBSTRING
# ==========================================================================
print('\n' + '='*80)
print('6. FINDING A SUBSTRING')
print('='*80)
# The .find() method returns the lowest index of the substring if it is found in the string. If the substring is not found, it returns -1.
index_world = message.find('World')
print('Print the starting index of \'World\' in message string:', index_world) # Output: 7
index_python = message.find('Python')
print('Print the starting index of \'Python\' in message string (not found):', index_python) # Output: -1

# ==========================================================================
# 7. REPLACING A SUBSTRING
# ==========================================================================
print('\n' + '='*80)
print('7. REPLACING A SUBSTRING')
print('='*80)
# The .replace() method returns a new string where all occurrences of a specified substring are replaced with another substring. It takes two arguments: the substring to be replaced and the substring to replace it with.
new_message = message.replace('World', 'Python')
print('Print the message string after replacing \'World\' with \'Python\':', new_message) # Output: Hello, Python!
remove_exclamation = message.replace('!', '')
print('Print the message string after removing exclamation mark:', remove_exclamation) # Output: Hello, Python

# ==========================================================================
# 8. STRING CONCATENATION AND INTERPOLATION(INSERTING VARIABLES AND EXPRESSIONS INTO STRINGS)
# ==========================================================================
print('\n' + '='*80)
print('8. STRING CONCATENATION AND INTERPOLATION(INSERTING VARIABLES AND EXPRESSIONS INTO STRINGS)')
print('='*80)
# String concatenation is the operation of joining two or more strings together. In Python, this can be done in multiple ways:
greeting = 'Hello'
name = 'Alice'
### 1. Using the + operator
greeting_message = greeting + ',' + ' ' + name + '!'
print('Print the greeting message using + operator:', greeting_message)  # Output: Hello, Alice!
# 2. Using .format() method
greeting_message_format = '{}, {}! Welcome to Python.'.format(greeting, name)
print('Print the greeting message using .format() method:', greeting_message_format)  # Output: Hello, Alice! Welcome to Python.
# 3. Using formatted string literals (f-strings)
greeting_message_fstring = f'{greeting}, {name}! How are you?'
print('Print the greeting message using f-string:', greeting_message_fstring)  # Output: Hello, Alice! How are you?
# 3.1 Using f-strings with expressions and String methods
age = 30
greeting_message_fstring_expr = f'{greeting}, {name.upper()}! Next year, you will be {age + 1} years old.'
print('Print the greeting message using f-string with expressions and String methods:', greeting_message_fstring_expr)  # Output: Hello, ALICE! Next year, you will be 31 years old.
# 4. Using the .join() method
greeting_message_join = ' '.join([greeting + ',', name + '!'])
print('Print the greeting message using join() method:', greeting_message_join)  # Output: Hello, Alice!
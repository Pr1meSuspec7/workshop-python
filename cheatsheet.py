# Data Types
int_num = 42
float_num = 3.14
string_var = "Hello, Python!"
bool_var = True

# Variables and Assignment
x = 10
y = "Python"

# Lists & Tuples
my_list = [1, 2, 3, "Python"]
my_tuple = (1, 2, 3, "Tuple")

# Dictionaries
my_dict = {'name': 'John', 'age': 25, 'city': 'Pythonville'}

# Control Flow
if x > 0:
    print("Positive")
elif x == 0:
    print("Zero")
else:
    print("Negative")

for item in my_list:
    print(item)

while True:
    print('Infinite Loop')
    break

# Functions
def greet(name="User"):
    return f"Hello, {name}!"

result = greet("John")

# Classes & Objects
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(f"{self.name} says Woof!")

my_dog = Dog("Buddy")
my_dog.bark()

# File Handling
with open("file.txt", "r") as file:
    content = file.read()

with open("new_file.txt", "w") as new_file:
    new_file.write("Hello, Python!")

with open("file.txt", "a") as file:
    new_file.write("Hello, Python again!")

# Exception Handling
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
finally:
    print("Execution completed.")

# Libraries & Modules
import math
from datetime import datetime
result = math.sqrt(25)
current_time = datetime.now()

# List Comprehensions
squares = [x**2 for x in range(5)]

# Lambda Functions
add = lambda x, y: x + y
result = add(2, 3)

# Virtual Environment
"""
# Create a virtual environment
python -m venv myenv

# Activate the virtual environment
source myenv/bin/activate  # On Unix or MacOS
myenv\Scripts\activate  # On Windows

# Deactivate the virtual environment
deactivate
"""

# Package Management
"""
# Install a package
pip install package_name

# List installed packages
pip list

# Create requirements.txt
pip freeze > requirements.txt

# Install packages from requirements.txt
pip install -r requirements.txt
"""

# Working with JSON
import json
data = {'name': 'John', 'age': 30}
# Convert Python object to JSON
json_data = json.dumps(data)
# Convert JSON to Python object
python_object = json.loads(json_data)

# Regular Expressions
import re
pattern = r'\d+'  # Match one or more digits
result = re.findall(pattern, "There are 42 apples and 123 oranges.")

# Working with Dates
from datetime import datetime, timedelta
current_date = datetime.now()
future_date = current_date + timedelta(days=7)

# List Manipulations
numbers = [1, 2, 3, 4, 5]
# Filter
evens = list(filter(lambda x: x % 2 == 0, numbers))
# Map
squared = list(map(lambda x: x**2, numbers))
# Reduce (requires functools)
from functools import reduce
product = reduce(lambda x, y: x * y, numbers)

# Dictionary Manipulations
my_dict = {'a': 1, 'b': 2, 'c': 3}
# Get value with default
value = my_dict.get('d', 0)
# Dictionary comprehension
squared_dict = {key: value**2 for key, value in my_dict.items()}

# Error Handling
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"Unexpected Error: {e}")
else:
    print("No errors occurred.")
finally:
    print("This block always executes.")

# Python Decorators
def decorator(func):
    def wrapper():
        print("Before function execution")
        func()
        print("After function execution")
    return wrapper
@decorator
def my_function():
    print("Inside the function")
my_function()

# Sending Email with smtplib
import smtplib
from email.mime.text import MIMEText
# Set up email server
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
# Log in to email account
server.login('your_email@gmail.com', 'your_password')
# Send email
msg = MIMEText('Hello, Python!')
msg['Subject'] = 'Python Email'
server.sendmail('your_email@gmail.com', 'recipient@example.com', msg.as_string())

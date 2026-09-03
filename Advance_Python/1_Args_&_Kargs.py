"""
DEFINITIONS:

1. *args (Non-Keyword Arguments / Positional Arguments):
   - The asterisk (*) is the unpack/pack operator. "args" is just a naming convention.
   - It allows a function to accept ANY NUMBER of positional arguments.
   - Inside the function, Python stores them as a TUPLE.

2. **kwargs (Keyword Arguments):
   - The double asterisk (**) packs named/keyword arguments.
   - It allows a function to accept ANY NUMBER of keyword arguments (key=value pairs).
   - Inside the function, Python stores them as a DICTIONARY.

ORDER OF PARAMETERS IN A FUNCTION:
   def func(standard_args, *args, default_args=value, **kwargs):
       ...
"""

def addition(*args):
    sum =0
    for i in args:
        sum = sum + i
    return sum

print(addition(1,2,23,4,5,6,7,8,6,554,4,3,3))


def details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Calling the function with keyword arguments

details(name="John", age=30, city="New York")

def info(**kwargs):
    return kwargs

print(info(name="ansari", age = 23 , city= "delhi",graduated = False))
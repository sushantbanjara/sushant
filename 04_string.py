"""
© https://sudipghimire.com.np


String Exercise


Please read the note carefully and try to solve the problem below:


"""

"""
1. Create two variablrs first_name, and last_name and print the sentence in the format below:
   suppose first_name is John and last_name is Doe
   "My name is John Doe"

   a. use + operator to concatenate strings
   b. use format() method to achieve the same result
   c. use f-strings to achieve the same result
   d. use %s formatting method to achieve the same result
"""
# answer 1
first_name = 'sushant'
last_name = 'banjara'

# 1.a
line1 = ('My name is ' + first_name + ' ' + last_name)
print(line1)


# 1.b
line2 = ('My name is {} {}'.format(first_name, last_name))
print(line2)


# 1.c
line3 = (f'My name is {first_name} {last_name}')
print(line3)


# 1.d
line4 = ('My name is %s %s'%(first_name, last_name))
print(line4)


"""
2. Assign a variable  pi and assign value 3.14159265
    a. use formatting strings to show pi with 3 digits after the decimal
    b. use formatting strings to show pi with 2 digits after the decimal but
       allocate 10 spaces for the variable
    c. use f-string to show the result in the following format:
        "The value of PIE is        3.14"

        hint: "%<a>.<b>f"
"""
# answer 2
pi = 3.14159265
# a
print('%5.3f'%pi)

# b
print('{:15.3f}'.format(pi))


# c
print(f'The value of pie is {pi:15.3f}')


"""
3. Use a function `input()`  to input the the name and age from the command line and
   display the formatted text as instructed below:

   a. use `input()` function to ask the name to the user. The console should show
      "What is your name?" to input the name
   b. similarly ask the user to input the age and assign it to another variable.

   c. Show a sentence describing the user name and age using different formatting methods.

      hint: Output would be a sentence similar to "Hello 20 years old John!!".
"""

# answer 3


# %%

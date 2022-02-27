"""
© https://sudipghimire.com.np

Type-casting and Hinting Exercises

Please read the note carefully and try to solve the problem below:

"""


"""
1. Type Hinting
    a. create a variable <odd> with hinting as `int` and assign a value to it.
    b. create a variable <PI> with hinting as `float` and assign 3.1415 to it.

    c. create any variable with `string` type hinting and assign `integer` value to it.
        - Check whether the program gives error in execution or not.
        - If it gives or does not give error, then why it gives or does not give error?
"""

# Answer 1a
odd : int = 9
print(odd)

# Answer 1b
PI : float = 3.1415
print(PI)

# Answer 1c
numbers : str = 5
print(numbers)
#It doesn't give error because number if the assigned value is not a string it just ignores the hinting.

"""
2. Type Conversion
"""
# ----------------------------------------[ a ]-----------------------------------------------

PI = 3.1415
# I want to print the value of PI to be 3. How should I convert the data to an integer
PI = int(PI)
print(PI)


# ----------------------------------------[ b ]-----------------------------------------------

str_1 = "20"
str_2 = "30"

print(str_1 + str_2)
# above line gives us output of "2030" but I want the answer to be 50.
# How would you solve the problem using type conversion?
str_1 = int(str_1)
str_2 = int(str_2)
print(str_1 + str_2)


# ----------------------------------------[ c ]-----------------------------------------------
x = ['1', '2', '3', '4', '5']
sum = 0
"""
- I want the value of sum to be 15.
- The way I get 15 is by adding all items from the list `x`.

Hint: the addition may involve
- for loops in the list
- type conversion
"""
for num in x:
    num = int(num)
    sum = sum + num
print(sum)


# ----------------------------------------[ d ]-----------------------------------------------
odd = [1, 3, 5, 7, 9, 11, 13, 15]
prime = [2, 3, 5, 7, 11, 13, 17]

"""
use type conversion to these lists to appropriate data type and find out
    - numbers that are odd but not prime
    - numbers that are either odd or prime
    - numbers that are prime but not odd.

Final values should be converted into list again and stored to variables.
"""
odd = set(odd)
print(odd)
prime = set(prime)
print(prime)
odd_not_prime = odd.difference(prime)
print(list(odd_not_prime))
odd_prime = odd.union(prime)
print(list(odd_prime))
prime_not_odd = prime.difference(odd)
print(list(prime_not_odd))
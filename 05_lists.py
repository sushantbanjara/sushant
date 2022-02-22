"""
© https://sudipghimire.com.np

Lists Exercises

Please read the note carefully and try to solve the problem below:

"""

"""
1. Write a program to create an empty list named `my_list` and

    a. add numbers 5 and 9 to the list using `append()` method

    b. ask the user to input any number in the console and add the number to the list.
        - you can use int() to change the type from string to integer if you want.

    c. create another list `more_items` with 3 items on it and extend the list `my_list`
        using `extend` method.

    d. now find the length of the list and print the length of list describing it in a sentence.
        - you can always use string formatting for better outputs.

    e. now remove the second item using `pop()` method and see if the item exists in the list
        - you can print the list before and after using the `pop()` method.
"""
# answer 1

my_list = []

# a

my_list.append(5)
my_list.append(9)
print(my_list)

# b

new_number = input("Enter a number: ")
new_number = int(new_number)
my_list.append(new_number)
print(my_list)

# c

more_items = [3, 6, 7]
my_list.extend(more_items)
print(my_list)

# d

len_list = len(my_list)
print(len_list)
len_list1 = my_list.__len__()
print(len_list1)
print(f"Number of items in the list is {len_list}")

# e

print(my_list)
my_list.pop(1)
print(my_list)



"""
2. Write a program to add 5 different wild animals to a list named `wild`.
    - tiger, lion, deer, bear, zebra

    a. sort them in ascending using the `sort()` method.
    b. reverse the list using the `reverse()` method.
    c. now add 3 more animals to the list `wild`.  ['leopard', 'elephant', 'rhino']
    d. find the position of `leopard` using the `index()` method and remove  it using `the pop()` method.
        - pop should have the index value returned using the `index()` method.
        - do not hard-code the position of leopard by manually counting it from the list.
        - check whether the leopard is removed from the list or not by `index()` method again.
          if the value error occurs, you have successfully removed it from the list.
          otherwise, try to do it again.
        - you can then comment the line that gives exception to continue to the next question.
    e. Now add `leopard` agin in the index 2 using `insert()` method.
    f. Again, remove `rhino` from the list using remove() method.

    note: you can print the values of list after each successful operations to see what is being changed.
"""
# answer 2
wild = ['tiger', 'lion', 'deer', 'bear', 'zebra']

# a
wild.sort()
print(wild)

# b
wild.reverse()
print(wild)

# c
wild.extend(('leopard','elephant','rhino'))
print(wild)

# d
f_leo = wild.index('leopard')
print(f_leo)
wild.pop(f_leo)
#f_leo_again = wild.index('leopard')

# e
wild.insert(2,'leopard')
print(wild)


# f
wild.remove('rhino')
print(wild)



"""
3. Try creating a multi-dimensional list or nested list `multi` of different numbers.
    eg: [[12,52,37],[46,51,16],[17,82,39]]

    a. access the number 51 from the list.
    b. access the number 82 using the negative indices.
    c. append another list [40, 61, 10] inside the list `multi`.
        the final list should be: [[12,52,37],[46,51,16],[17,82,39],[40, 61, 10]]
    d. use foreach in the list `multi` to print each list item to the console.
        - Bonus: try using nested foreach to access each item inside of the inner list
    e. finally clear the list `multi` using the `clear()` method and verify if the list is empty or not
"""
# answer 3
multi = [[12,52,37],[46,51,16],[17,82,39]]

# a
print(multi[1][1])

# b
print(multi[-1][-2])

# c
multi.append([40, 61, 10])
print(multi)

# d
for items in multi:
    print(items)
    for i in items:
        print(i)

# e
multi.clear()
print(multi)
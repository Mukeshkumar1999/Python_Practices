print("Radhe Radhe")

# a = 10
# b = 20
# print(a+b)
# print("val of a", a)

# def showName(str):
#     print(str)
# showName("Radhe Radhe")

# write program to add two number
'''
def addNum(a,b):
    return a+b

print(addNum(10,20))
'''   #multiline comments

# for loop
'''
for i in range(0,10):
    print("val of i", i)
'''
# print number 1 to 10 using function
'''
def tablePrint(a, st,end):
    for i in range(st,end):
        print('Table of ',a,'*',i,':', a * i )
tablePrint(2,1,11)

'''
# print fibbonacci series
# 0,1,1,2,3,5,8,13....
'''
a = 0
b = 1

for i in range(0,4):
    print(a)
    c = a+b;
    a = b
    b = c
'''
# types of Variable in python
'''
1. Numeric Types:
Integers (int): Whole numbers (e.g., 5, -100).
Floats (float): Numbers with decimal points (e.g., 3.14, -0.5).
Complex Numbers (complex): Numbers with a real and an imaginary part (e.g., 2 + 3j).
2. Sequence Types:
Strings (str): Ordered sequences of characters (e.g., "hello", 'Python').
Lists (list): Ordered, mutable collections of items (e.g., [1, 2, "apple"]).
Tuples (tuple): Ordered, immutable collections of items (e.g., (10, 20, 30)).
3. Set Types:
Sets (set): Unordered collections of unique items (e.g., {"red", "green", "blue"}).
Frozensets (frozenset): Immutable versions of sets.
4. Mapping Type:
Dictionaries (dict): Unordered collections of key-value pairs (e.g., {"name": "Alice", "age": 30}).
5. Boolean Type:
Booleans (bool): Represents logical values, either True or False.
6. None Type:
NoneType: Represents the absence of a value, with the single value None.
'''

# Examples

print(2.50)  # float numbers

# Assigning Different Values
'''
x,y,z = 2,100.1,"Jai Shri Krishna"
print(x,y,z)
'''

#  Casting variables

# 1. string to integer casting
s = "100"
n = int(s)
print(n)
# 2. integer to string casting
val = 20
s1 = str(val);
print(s1)

# integer to float casting

val2 = float(val)
print(val2)

# how to find types of variables

print(type(n))
print(type(s1))
print(type(val2))

# scape variable in python
# '/n' its mean print new line its call scape variable
'''
print("Jai shree Krishna"'\n'"jai Shri Radha Rani")
'''

# Swapping Two Variables
'''
g, h = 10 , 30
print(g,h)
g,h  = h,g
print(g,h)
'''

# count character of words
'''
s = "radha radha"
print(len(s))   # total length of s string is 11 including white space
'''

# Concatenate two string
'''
s3 = "Hare Radha"
s4 = "Hare Krishna"
print(s3 +" "+ s4)
'''
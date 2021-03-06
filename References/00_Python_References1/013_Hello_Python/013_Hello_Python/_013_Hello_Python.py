
# ---------- ITERABLES ----------
# An iterable is a stored sequence of values (list) or,
# as we will see when we cover generators, an
# object that produces one value at a time
 
# Iterables differ from iterators in that an iterable
# is an object with an __iter__ method which returns
# an iterator. An iterator is an object with a
# __next__ method which retrieves the next value from
# sequence of values
 
# Define a string and convert it into an iterator
sampStr = iter("Sample")
 
print("Char :", next(sampStr))
print("Char :", next(sampStr))
 
# You can add iterator behavior to your classes
class Alphabet:
 
    def __init__(self):
        self.letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.index = -1
 
    def __iter__(self):
        return self
 
    def __next__(self):
        if self.index >= len(self.letters) - 1:
            raise StopIteration
        self.index += 1
        return self.letters[self.index]
 
alpha = Alphabet()
 
for letter in alpha:
    print(letter)
 
# Iterate through a dictionary because it is an iterable
derek = {"fName": "Derek", "lName": "Banas"}
 
for key in derek:
    print(key, derek[key])
 
# ---------- PROBLEM ----------
# Create a class that returns values from the Fibonacci
# sequence each time next is called
# Sample Output
# Fib : 1
# Fib : 2
# Fib : 3
# Fib : 5
 
class FibGenerator:
 
    def __init__(self):
        self.first = 0
        self.second = 1
 
    def __iter__(self):
        return self
 
    def __next__(self):
        fibNum = self.first + self.second
        self.first = self.second
        self.second = fibNum
        return fibNum
 
fibSeq = FibGenerator()
 
for i in range(10):
    print("Fib :", next(fibSeq))
 
# ---------- LIST COMPREHENSIONS ----------
# A list comprehension executes an expression against an iterable
 
# Note: While they are super powerful, try not to make list
# comprehensions that are hard to figure out for others
 
# To multiply 2 times every value with a map we'd do
print(list(map((lambda x: x * 2), range(1, 11))))
 
# With a list comprehension we'd do
# Note that a list comprehension is surrounded by []
# because it returns a list
print([2 * x for x in range(1, 11)])
 
# To construct a list of odds using filter we'd
print(list(filter((lambda x: x % 2 != 0), range(1, 11))))
 
# To do the same with a list comprehension
print([x for x in range(1, 11) if x % 2 != 0])
 
# A list comprehension can act as map and filter
# on one line
# Generate a list of 50 values and take them to the power
# of 2 and return all that are multiples of 8
 
print([i ** 2 for i in range(50) if i % 8 == 0])
 
# You can have multiple for loops as well
# Multiply all values in one list times all values in
# another
print([x * y for x in range(1, 3) for y in range(11, 16)])
 
# You can put list comprehensions in list comprehensions
# Generate a list of 10 values, multiply them by 2 and
# return multiples of 8
print([x for x in [i * 2 for i in range(10)] if x % 8 == 0])
 
# ---------- PROBLEM ----------
# Generate a list of 50 random values between 1 and 1000
# and return those that are multiples of 9
# You'll have to use a list comprehension in a list comprehension
# This is a hard one!
 
import random
 
print([x for x in [random.randint(1, 1001) for i in range(50)] if x % 9 == 0])
 
# List comprehensions also make it easy to work with
# multidimensional lists
 
multiList = [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]]
 
print([col[1] for col in multiList])
 
# Get the diagonal by incrementing 0, 0 -> 1, 1 -> 2, 2
print([multiList[i][i] for i in range(len(multiList))])
 
# ---------- GENERATOR FUNCTIONS ----------
# A generator function returns a result generator when called
# They can be suspended and resumed during execution of
# your program to create results over time rather then
# all at once
 
# We use generators when we want to big result set, but
# we don't want to slow down the program by creating
# it all at one time
 
# Create a generator that calculates primes and returns
# the next prime on command
 
def isprime(num):
    # This for loop cycles through primes from 2 to
    # the value to check
    for i in range(2, num):
 
        # If any division has no remainder we know it
        # isn't a prime number
        if (num % i) == 0:
            return False
    return True
 
# This is the generator
def gen_primes(max_number):
 
    # This for loop cycles through primes from 2 to
    # the maximum value requested
    for num1 in range(2, max_number):
 
        if isprime(num1):
 
            # yield is what makes this a generator
            # When called by next it will return the
            # next result
            yield num1
 
# Create a reference to the generator
prime = gen_primes(50)
 
# Call next for each result
print("Prime :", next(prime))
print("Prime :", next(prime))
print("Prime :", next(prime))
 
# ---------- GENERATOR EXPRESSIONS ----------
# Generator expressions look just like list comprehensions
# but they return results one at a time
# The are surrounded by parentheses instead of [ ]
 
double = (x * 2 for x in range(10))
 
print("Double :", next(double))
print("Double :", next(double))
 
# You can iterate through all results as well
for num in double:
    print(num)

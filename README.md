# -Plane-Tickets
Introduction
A generator is a function or expression that returns a special type of iterator called generator iterator. Generator-iterators are lazy: they do not store their values in memory, but generate their values when needed.

A generator function looks like any other function, but contains one or more yield expressions. Each yield will suspend code execution, saving the current execution state (including all local variables and try-statements). When the generator resumes, it picks up state from the suspension - unlike regular functions which reset with every call.

Constructing a generator
Generators are constructed much like other looping or recursive functions, but require a yield expression, which we will explore in depth a bit later.

An example is a function that returns the squares from a given list of numbers. As currently written, all input must be processed before any values can be returned:

>>> def squares(list_of_numbers):
...     squares = []
...     for number in list_of_numbers:
...         squares.append(number ** 2)
...     return squares
You can convert that function into a generator like this:

>>> def squares_generator(list_of_numbers):
...     for number in list_of_numbers:
...         yield number ** 2
The rationale behind this is that you use a generator when you do not need to produce all the values at once. This saves memory and processing power, since only the value you are currently working on is calculated.

Using a generator
Generators may be used in place of most iterables in Python. This includes functions or objects that require an iterable/iterator as an argument.

To use the squares_generator() generator:

>>> squared_numbers = squares_generator([1, 2, 3, 4])

>>> for square in squared_numbers:
...     print(square)
...
1
4
9
16
Values within a generator can also be produced/accessed via the next() function. next() calls the __next__() method of a generator-iterator object, "advancing" or evaluating the code up to its yield expression, which then "yields" or returns a value:

>>> squared_numbers = squares_generator([1, 2])

>>> next(squared_numbers)
1
>>> next(squared_numbers)
4
When a generator-iterator is fully consumed and has no more values to return, it throws a StopIteration error.

>>> next(squared_numbers)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
Note
Generator-iterators are a special sub-set of iterators. Iterators are the mechanism/protocol that enables looping over iterables. Generator-iterators and the iterators returned by common Python iterables act very similarly, but there are some important differences to note:

They are lazily evaluated; iteration is one-way and there is no "backing up" to a previous value.
They are consumed by iterating over the returned values; there is no resetting or saving in memory.
They are not sortable and cannot be reversed.
They are not sequence types, and do not have indexes. You cannot reference a previous or future value using addition or subtraction and you cannot use bracket ([]) notation or slicing.
They cannot be used with the len() function, as they have no length.
They can be finite or infinite - be careful when collecting all values from an infinite generator-iterator!
The yield expression
The yield expression is very similar to the return expression. Unlike the return expression, yield gives up values to the caller at a specific point, suspending evaluation/return of any additional values until they are requested. When yield is evaluated, it pauses the execution of the enclosing function and returns any values of the function at that point in time. The function then stays in scope, and when __next__() is called, execution resumes until yield is encountered again.

Note
Using yield expressions is prohibited outside of functions.

>>> def infinite_sequence():
...     current_number = 0
...     while True:
...         yield current_number
...         current_number += 1

>>> lets_try = infinite_sequence()
>>> lets_try.__next__()
0
>>> lets_try.__next__()
1
Why Create a Generator?
Generators are useful in a lot of applications.

When working with a potentially large collection of values, you might not want to put all of them into memory. A generator can be used to work on larger data piece-by-piece, saving memory and improving performance.

Generators are also very helpful when a process or calculation is complex, expensive, or infinite:

>>> def infinite_sequence():
...     current_number = 0
...     while True:
...         yield current_number
...         current_number += 1
Now whenever __next__() is called on the infinite_sequence object, it will return the previous number + 1.

Instructions
Conda Airlines is the programming-world's biggest airline, with over 10,000 flights a day!

They are currently assigning all seats to passengers by hand; this will need to be automated.

They have asked you to create software to automate passenger seat assignments. They require your software to be memory efficient and performant.

Conda wants to generate seat letters for their airplanes. An airplane is made of rows of seats. Each row has 4 seats. The seats in each row are always named A, B, C, and D. The first seat in the row is A, the second seat in the row is B, and so on. After reaching D, it should start again with A.

Implement a function generate_seat_letters(<number>) that accepts an int that holds how many seat letters to be generated. The function should then return an iterable of seat letters.

>>> letters = generate_seat_letters(4)
>>> next(letters)
"A"
>>> next(letters)
"B"

Stuck? Reveal Hints
Opens in a modal

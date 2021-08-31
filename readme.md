# Part 1: The Factorial Function
Let's start with writing a function to calculate the factorial of a number

_The Factorial of a whole number greater than 1 is the product of all whole numbers from 1 to itself (1 and itself included). The '!' sign is used to denote factorial notation._

e.g. 
> 1! = 1

> 2! = 1 * 2 = 2

> 3! = 1 * *2* * 3 = 6

and so on

So our factorial function needs to accept a positive integer as input and calculate the product of all positive integers from one to that number.

We can do this is many ways

a) using a for loop in inside the function
```py
def factorial_funct(n):
  """define a variable called product. We can't set it as 0, as anything multiplied by 0, will always return 0."""

  product = 1

  for num in range(1,n+1):
    product *= num

  return product
```
b) using recursion
```py
def recursive_factorial(n):
  return n * recursive_factorial(n-1)
```
This is cleaner and shorter code, however when you run this, the interpreter throws a Recursion error:
>return n * recursive_factorial(n-1)

>[Previous line repeated 996 more times]

>RecursionError: maximum recursion depth exceeded

The function goes into an endless loop, since the lower limit for n-1 is not defined and you can keep on subtracting 1 from an integer till negative infinity.

Let's set some constraints in our recursive_factorial function:
```py
def recursive_factorial(n):
  if n>1:
    return n * recursive_factorial(n-1)
  else:
    return 1
```
We `return 1` rather than '0' in the else statement, so that the product till the statement is triggered remains unchanged (anything multiplied by 1 is itself, but anything multiplied by 0, is 0).

Now let's add code for accepting the number for which you want to determine the factorial as input
```py
num = input('Enter a positive integer for which you want to calculate the factorial)
```

Since python treats any input as string type, we need to convert the input to integer type before using in the function.

```py
print(f"The factorial of {num} using the factorial_funct function is {factorial_funct(int(num))}.")

print(f"The factorial of {num} using the recursive_factorial function is {recursive_factorial(int(num))}.")
```
***

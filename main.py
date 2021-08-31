def factorial_funct(n):
  """define a variable called product. We can't set it as 0, as anything multiplied by 0, will always return 0."""
  
  product = 1

  for num in range(1,n+1):
    product *= num

  return product


def recursive_factorial(n):
  if n>1:
    return n * recursive_factorial(n-1)
  else:
    return 1
  
num = input('Enter a positive integer for which you want to calculate the factorial: \n')

print(f"The factorial of {num} using the factorial_funct function is {factorial_funct(int(num))}.")

print(f"The factorial of {num} using the recursive_factorial function is {recursive_factorial(int(num))}.")
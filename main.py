# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.
def greet():
  print("Hello!")
  print("I am a function.")
  print("Isn't the weather nice today?")

#greet()

def greet_name(name):
  print(f"Hello {name}")
  print(f"I am a function, {name}")

#greet_name("Jamie")

def sum(x, y):
  return(x + y)

num1 = int(input("first number: "))
num2 = int(input("second number: "))

print(sum(num1, num2))
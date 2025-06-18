def myfunc():
  x = 10   # x exists only inside this function (local)
  print(x)

myfunc()
print(x)  # n error — x is not defined here!


# Function inside a function:
def myfunc():
  x = 300         # Local variable in myfunc()

  def myinnerfunc():
    print(x)      # x is accessible here

  myinnerfunc()

myfunc()

# Global variable:
x = 300        # global variable

def myfunc():
  print(x)     # x is accessible inside the function

myfunc()
print(x)       # x is also accessible outside the function

# The same variables: inside and outside

x = 300      # Global variable

def myfunc():
  x = 200    # Local variable (different from global x)
  print(x)   # the local x = 200

myfunc()
print(x)     # prints the global x = 300

# Global keyword:

def myfunc():
  global x
  x = 300      # This creates or changes the global x even tho its inside a func

myfunc()

print(x)       # This works — x is global now

# Non-local keyword:

def myfunc1():
  x = "Jane"         # Local to myfunc1()

  def myfunc2():
    nonlocal x       # Now x refers to the x in myfunc1
    x = "hello"      # Changes x in myfunc1

  myfunc2()
  return x

print(myfunc1())     # Output: hello


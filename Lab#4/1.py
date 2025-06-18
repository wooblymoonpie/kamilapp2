mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))  # prints "apple"
print(next(myit))  # prints "banana"
print(next(myit))  # prints "cherry"

''' 
iter(mytuple) gives us an iterator.

next(myit) gives the next item from the iterator.
'''
# STRING:
mystr = "banana"
myit = iter(mystr)

print(next(myit))  # 'b'
print(next(myit))  # 'a'
print(next(myit))  # 'n'
print(next(myit))  # 'a'
print(next(myit))  # 'n'
print(next(myit))  # 'a'

''' 
iter(mystr) creates an iterator from the string "banana".

Each call to next(myit) gives the next character from the string.
'''
# FOR:
mytuple = ("apple", "banana", "cherry")

for x in mytuple:
  print(x)

''' 
Python turns mytuple into an iterator using iter().

Then, for each step, it uses next() to get the next value and assigns it to x.
'''

# Creating an Iterator:
class MyNumbers:
  def __iter__(self):
    self.a = 1  # Initialize the starting number
    return self  # Return the iterator object itself

  def __next__(self):
    x = self.a       # Store current value
    self.a += 1      # Increment for the next time
    return x         # Return current value
  
  myclass = MyNumbers()       # Create object
  myiter = iter(myclass)      # Get iterator from object
  print(next(myiter))  # 1
  print(next(myiter))  # 2
  print(next(myiter))  # 3
  print(next(myiter))  # 4
  print(next(myiter))  # 5

# StopIteration:
  def __next__(self):
  if self.a > 5:
    raise StopIteration
  x = self.a
  self.a += 1
  return x
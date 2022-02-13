# PyExecSpeed

A simple package for calculating the execution time of a function in a Python file

## Usage:

* `speed.showSpeed(function, r)`
  where `function` is any function from your Python file and `r` is the number of times to run it. 
  Prints average execution time.

* `speed.getSpeed(function, r)`
  again, `function` is any function from your Python file and `r` is the number of times to run it. 
  Returns average execution time as a float.

## Example:
```py
import speed

def myFunc():
  x = 2
  for i in range(100):
    x *= i
  print(x)

n = 10
speed.showSpeed(myFunc, n) 
# Repeats myFunc n (= 10) times and prints the average execution time. 
# A higher value of n will likely result in a more accurate value, but will take longer.


>>> 0.00003339
```

### Notes:

* The output from `getSpeed()` is a float.
* While `showSpeed()` or `getSpeed()` run a function, they block printing within that function so the terminal isn't filled with potentially hundreds of prints.
* Currently, passing arguments into the `function` argument e.g. `showSpeed(myFunc(a,b), 100)` **doesn't** work. I'll add this soon, with the syntax: `showSpeed(function, r, <other>, <arguments>, <here>...)`, which will check the execution time of `function(other, arguments, here...)`


### [Create an issue](https://github.com/Astrochamp/speed/issues) if you have any feedback / bugs you want to report
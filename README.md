# PyExecSpeed

A simple package for calculating the execution time of a function in a Python file

## Usage:

### Installation
`pip install execspeed`

### Using
* `speed.showSpeed(function, r, <optional>, <extra>, <args>...)`
  where `function` is any function from your Python file and `r` is the number of times to run it. 
  Prints average execution time.

* `speed.getSpeed(function, r, <optional>, <extra>, <args>...)`
  again, `function` is any function from your Python file and `r` is the number of times to run it. 
  Returns average execution time as a float.

## Example:
```py
import speed

def myFunc(start, message):
  x = start
  for i in range(100):
    x *= i
  print(f"{message} {x}")

n = 10
speed.showSpeed(myFunc, n, 3, "Your number is:") 
# Repeats myFunc n (= 10) times and prints the average execution time.
# Passed (3) and "Your number is:" to myFunc() -- any number of arguments can now be passed to your function this way 
# A higher value of n will likely result in a more accurate value, but will take longer.


>>> 0.00003339
```

### Notes:

* The output from `getSpeed()` is a float.
* While `showSpeed()` or `getSpeed()` run a function, they block printing within that function so the terminal isn't filled with potentially hundreds of prints.


### [Create an issue](https://github.com/Astrochamp/speed/issues) if you have any feedback / bugs you want to report
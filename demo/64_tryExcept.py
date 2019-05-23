# The finally block gets executed no metter, if try block raises an errors or not.

try:
    print(x)
except:
    print("Someting went wrong")
finally:
    print("The 'try except' is finished")
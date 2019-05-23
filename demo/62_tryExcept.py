# The try block will generate an error, because x is not defined and print also exception handling message

try:
    print(x)

except Exception as e:
    print("Something else went wrong")
    print(e)
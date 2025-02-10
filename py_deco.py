def begend(func):
    def wrapper(*args):
        print("Begin testing\n")
        result = func(*args)
        print("\nEnd testing")
        return result
    return wrapper

@begend
def testing():
    print("This is the function being tested")

testing()
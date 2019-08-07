def my_method(arg1, arg2):
    return arg1 + arg2

my_method(5, 6)

def my_long_method(arg1, arg2, arg3, arg4, arg5):
    return arg1 + arg2 + arg3 + arg4 + arg5

def addition_simplified(*args):
    return sum(args)

print(addition_simplified(2, 2))
print(addition_simplified(4, 5, 6, 7, 8, 9, 7))

def what_are_kwargs(*args, **kwargs):
    print(args)
    print(kwargs)


what_are_kwargs(12, 22, 33, name = 'Pioter', location = 'Polszcza')

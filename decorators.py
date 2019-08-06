import functools

def my_decorator(func):
    @functools.wraps(func)
    def function_that_runs_fun():
        print("In the decorator!")
        func()
        print("After the decorator!")
    return function_that_runs_fun

@my_decorator
def my_function():
    print("I'm in the function!")

##

def decorator_with_arguments(number):
    def my_decorator(func):
        @functools.wraps(func)
        def funtction_that_runs_func():
            print("In the decorator!");
            if number % 2 == 0:
                print("The parameter is even... Function running:")
                func()
            else:
                print("The parameter is odd... Function is not running!")
            print("After the decorator!")
        return funtction_that_runs_func
    return my_decorator


@decorator_with_arguments(90)
def my_function_too():
    print("That's me - my_function_too!")


my_function_too()


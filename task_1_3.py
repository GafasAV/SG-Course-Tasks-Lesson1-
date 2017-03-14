def decorator(enable=False):
    
    def decorate(fn):
        
        if not enable:
            return fn
    
        def wrapper(*args, **kwargs):
            try:
                result = fn(*args, **kwargs)
            except (ZeroDivisionError, Exception) as err:
                print("Exception occured in {0}: {1}".format(fn.__name__, err))
                print("Input args: {0}".format(args))
                print("Input kwargs: {0}".format(kwargs))
                return None
            else:
                return result

        return wrapper

    return decorate


@decorator(enable=True)
def func(x, y, **kwargs):
    return x / y


if __name__ == "__main__":

    res = func(10, 0, op="division", base=10)
    print("Result : {0} \n".format(res))

    res = func(10, 2, op="division", base=10)
    print("Result : {0} \n".format(res))

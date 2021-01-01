def exception_check(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("The Error!")
    else:
        print(result)

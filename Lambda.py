
# A Python lambda function behaves like a normal function in regard to arguments. 
# Therefore, a lambda parameter can be initialized with a default value: the parameter n takes the outer n 
# as a default value.

def dispatch_dict(operator, x, y):
    return {
        'add': lambda: x + y,
        'sub': lambda: x - y,
        'mul': lambda: x * y,
        'div': lambda: x / y,
    }.get(operator, lambda: None)()

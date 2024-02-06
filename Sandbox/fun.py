def tester(func):
    def wrapper(*args):
        print(f"Addition called with args {args}")
        result = func(*args)
        print(f"Result: {result}")
        return result

    return wrapper


@tester
def add(a: int, b: int) -> int:
    return a + b


a = add(1, 2)

b = add(a, 3)

print(a, b)

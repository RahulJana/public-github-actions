def _decorator(func):
    def _wrapper(*args, **kwargs):
        print("Before function call")
        func(*args, **kwargs)
        print("After function call")
    return _wrapper


@_decorator
def wave():
    print("👋")

wave()


def wave():
    print("👋👌")

wave()

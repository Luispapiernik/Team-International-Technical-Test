from typing import Callable, List

from data_capture.errors import InvalidTypeError, OutOfRangeError


def args_in_range(a: int, b: int) -> Callable:
    def decorator(obj_method: Callable) -> Callable:
        def wrapper(self, *args: List[int]):
            for number in args:
                if number < a or b < number:
                    raise OutOfRangeError("Number out of range")

            return obj_method(self, *args)

        return wrapper

    return decorator


def args_with_integer_type(obj_method: Callable) -> Callable:
    def wrapper(self, *args: List[int]):
        for number in args:
            if not isinstance(number, int):
                raise InvalidTypeError("All arguments must be of integer type")

        return obj_method(self, *args)

    return wrapper

from typing import Callable, List

from data_capture.errors import InvalidTypeError, OutOfRangeError


def args_in_range(a: int, b: int) -> Callable:
    """
    Decorator fabric
    """

    def decorator(obj_method: Callable) -> Callable:
        """
        Decorator that check that the arguments passed to the decorated function are
        between a given range.

        Parameters
        ----------
        obj_method: callable
            Function to be decorated, it must be a object method of numeric parameters
        """

        def wrapper(self, *args: List[int]):
            for number in args:
                if number < a or b < number:
                    raise OutOfRangeError("Number out of range")

            return obj_method(self, *args)

        return wrapper

    return decorator


def args_with_integer_type(obj_method: Callable) -> Callable:
    """
    Decorator that check that the arguments passed to the decorated function are
    integers.

    Parameters
    ----------
    obj_method: callable
        Function to be decorated, it must be a object method of numeric parameters
    """

    def wrapper(self, *args: List[int]):
        for number in args:
            if not isinstance(number, int):
                raise InvalidTypeError("All arguments must be of integer type")

        return obj_method(self, *args)

    return wrapper

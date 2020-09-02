import functools
from typing import Callable, TypeVar

T = TypeVar("T")


def client(name: str) -> Callable[..., Callable[..., T]]:
    """
    Use a service from the system. All the input and output data
    should be serializable.
    """

    def wrapper_builder(f: Callable[..., T]) -> Callable[..., T]:
        @functools.wraps(f)
        def wrapper(*args, **kw) -> T:
            return f(*args, **kw)

        return wrapper

    return wrapper_builder


def service(name: str) -> Callable[..., Callable[..., T]]:
    """
    Expose a service to the system. All the input and output data
    should be serializable.
    """

    def wrapper_builder(f: Callable[..., T]) -> Callable[..., T]:
        @functools.wraps(f)
        def wrapper(*args, **kw) -> T:
            return f(*args, **kw)

        return wrapper

    return wrapper_builder


def intercept(name: str) -> Callable[..., Callable[..., T]]:
    """
    Intercept service calls. All the inputs and output data should
    be serializable.
    """

    def wrapper_builder(f: Callable[..., T]) -> Callable[..., T]:
        @functools.wraps(f)
        def wrapper(*args, **kw) -> T:
            return f(*args, **kw)

        return wrapper

    return wrapper_builder

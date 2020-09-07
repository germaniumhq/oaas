import abc
from typing import TypeVar

T = TypeVar("T")


class ServerMiddleware(metaclass=abc.ABCMeta):
    """
    Defines a serialization provider that can interpret the
    registrations and invoke the methods.
    """

    @abc.abstractmethod
    def serve(self) -> None:
        ...

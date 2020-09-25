import abc
from typing import TypeVar

from oaas.service_definition import ServiceDefinition

T = TypeVar("T")


class ServerMiddleware(metaclass=abc.ABCMeta):
    """
    Defines a serialization provider that can interpret the
    registrations and invoke the methods.
    """

    @abc.abstractmethod
    def serve(self) -> None:
        ...

    @abc.abstractmethod
    def join(self) -> None:
        ...

    @abc.abstractmethod
    def can_serve(self, service: ServiceDefinition) -> bool:
        ...

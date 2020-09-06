import abc
from typing import Type, TypeVar

from oaas.client_definition import ClientDefinition

T = TypeVar("T")


class SerializationProvider(metaclass=abc.ABCMeta):
    """
    Defines a serialization provider that can interpret the
    registrations and invoke the methods.
    """

    @abc.abstractmethod
    def serve(self) -> None:
        ...

    @abc.abstractmethod
    def create_client(self, t: Type[T]) -> T:
        ...

    @abc.abstractmethod
    def can_handle(self, client_definition: ClientDefinition) -> bool:
        pass

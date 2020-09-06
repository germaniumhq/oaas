from typing import Type, Any

import oaas._registrations as registrations
from oaas.serialization_provider import SerializationProvider, T


class ReflectionInvoker:
    def __init__(self, *, delegate: Any) -> None:
        self._delegate = delegate

    def __getattr__(self, item):
        return getattr(self._delegate, item)


class LocalSerializationProvider(SerializationProvider):
    def __init__(self) -> None:
        self._service_instance = dict()

    def serve(self) -> None:
        for service_name, service_definition in registrations.services.items():
            self._service_instance[service_name] = service_definition.code()

    def create_client(self, t: Type[T]) -> T:
        client_definition = registrations.clients[t]
        service_instance = self._service_instance[client_definition.name]

        return ReflectionInvoker(delegate=service_instance)

    def can_handle(self, t: Type[T], *args, **kw) -> bool:
        return True

from typing import Any, Dict, cast, TypeVar

import oaas._registrations as registrations
from oaas.client_definition import ClientDefinition
from oaas.client_provider import ClientMiddleware
from oaas.server_provider import ServerMiddleware

T = TypeVar("T")


class ReflectionInvoker:
    def __init__(self, *, delegate: Any) -> None:
        self._delegate = delegate

    def __getattr__(self, item):
        return getattr(self._delegate, item)


class LocalClientServerMiddleware(ClientMiddleware, ServerMiddleware):
    """
    Provides a server that can invoke local services
    """

    def __init__(self) -> None:
        self._service_instance: Dict[str, Any] = dict()

    def serve(self) -> None:
        for service_definition, _ in registrations.services.items():
            self._service_instance[service_definition.name] = service_definition.code()

    def create_client(self, client_definition: ClientDefinition) -> T:
        service_instance = self._service_instance[client_definition.name]

        return cast(T, ReflectionInvoker(delegate=service_instance))

    def can_handle(self, client_definition: ClientDefinition) -> bool:
        return True

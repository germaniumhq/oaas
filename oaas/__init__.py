from typing import Callable, TypeVar, Type, Optional

import oaas._registrations as registrations
from oaas.client_definition import ClientDefinitionMetadata, ClientDefinition
from oaas.serialization_provider import SerializationProvider
from oaas.service_definition import ServiceDefinition, ServiceDefinitionMetadata

T = TypeVar("T")


def client(
    name: str, metadata: Optional[ClientDefinitionMetadata] = None
) -> Callable[..., Type[T]]:
    """
    Declare a service from the system. All the input and output data
    should be serializable. The serialization format depends on
    the provider being used. To get an instance to the client, call
    `get_client`.
    """

    def wrapper_builder(t: Type[T]) -> Type[T]:
        cd = ClientDefinition(
            name=name,
            code=t,
            metadata=metadata,
        )
        registrations.clients[t] = cd

        return t

    return wrapper_builder


def service(
    name: str, metadata: Optional[ServiceDefinitionMetadata] = None
) -> Callable[..., Type[T]]:
    """
    Mark a service to be exposed to the system. All the input
    and output data should be serializable. The serialization
    format depends on the provider being used.
    """

    def wrapper_builder(t: Type[T]) -> Type[T]:
        sd = ServiceDefinition(
            name=name,
            code=t,
            metadata=metadata,
        )
        registrations.services[sd] = True

        return t

    return wrapper_builder


def serve() -> None:
    """
    Expose all the defined services using the underlying
    providers.
    """
    # FIXME: If multiple providers are configured they should be
    # exposed and then joined.
    for provider in registrations.serialization_providers:
        provider.serve()


def get_client(t: Type[T]) -> T:
    """
    Create a client for the given type.
    """
    for provider in registrations.serialization_providers:
        client_definition = registrations.clients[t]
        if provider.can_handle(client_definition):
            return provider.create_client(client_definition)

    raise Exception(
        f"No serialization provider was registered to handle " f"{t} clients."
    )


def register_serialization_provider(serialization_provider: SerializationProvider):
    """
    Register a serialization provider. Normally this should be taken
    care by the midlleware.
    """
    registrations.serialization_providers.add(serialization_provider)

from typing import Dict, Set, Callable

from oaas.client_definition import ClientDefinition
from oaas.serialization_provider import SerializationProvider
from oaas.service_definition import ServiceDefinition

clients: Dict[Callable, ClientDefinition] = dict()
services: Dict[str, ServiceDefinition] = dict()

serialization_providers: Set[SerializationProvider] = set()

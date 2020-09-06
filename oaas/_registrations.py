from collections import OrderedDict
from typing import Dict, Set, Type

from oaas.client_definition import ClientDefinition
from oaas.serialization_provider import SerializationProvider
from oaas.service_definition import ServiceDefinition

clients: Dict[Type, ClientDefinition] = OrderedDict()
services: Dict[ServiceDefinition, bool] = OrderedDict()

serialization_providers: Set[SerializationProvider] = set()

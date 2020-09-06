from typing import Dict, Optional, Any, TypeVar, Type

ServiceDefinitionMetadata = Dict[str, Any]
T = TypeVar("T")


class ServiceDefinition:
    def __init__(
        self,
        *,
        name: str,
        code: Type[T],
        metadata: Optional[ServiceDefinitionMetadata] = None
    ) -> None:
        self.name = name
        self.code = code
        self.metadata = metadata

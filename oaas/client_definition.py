from typing import Dict, Optional, Any, TypeVar, Type

T = TypeVar("T")
ClientDefinitionMetadata = Dict[str, Any]


class ClientDefinition:
    def __init__(
        self,
        *,
        name: str,
        code: Type[T],
        metadata: Optional[ClientDefinitionMetadata] = None
    ) -> None:
        self.name = name
        self.code = code
        self.metadata = metadata

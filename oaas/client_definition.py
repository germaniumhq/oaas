from typing import Callable, Dict, Optional, Any

ClientDefinitionMetadata = Dict[str, Any]


class ClientDefinition:
    def __init__(
        self,
        *,
        name: str,
        code: Callable,
        metadata: Optional[ClientDefinitionMetadata] = None
    ) -> None:
        self.name = name
        self.code = code
        self.metadata = metadata

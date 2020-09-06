from typing import Callable, Dict, Optional, Any

ServiceDefinitionMetadata = Dict[str, Any]


class ServiceDefinition:
    def __init__(
        self,
        *,
        name: str,
        code: Callable,
        metadata: Optional[ServiceDefinitionMetadata] = None
    ) -> None:
        self.name = name
        self.code = code
        self.metadata = metadata

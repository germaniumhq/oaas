Container As A Service API

Installation
============

    pip install caas

Usage
=====

    from typing import Any, List

    import caas


    @caas.client("users-get")
    def get_users(group: str) -> List[Any]: ...


    @caas.client("datastore")
    class DataStore:
        def put_item(self, key: str, value: Any) -> None: ...

        def get_item(self, key: str) -> None: ...

        def remove_item(self, key: str) -> None: ...


    @caas.service("users-get")
    def get_user_list(group: str) -> List[Any]: ...


    @caas.service("datastore")
    class DataStoreService:
        def put_item(self, key: str, value: Any) -> None: ...

        def get_item(self, key: str) -> None: ...

        def remove_item(self, key: str) -> None: ...


    @caas.service("intercept")
    def get_user_intercept(group: str) -> List[Any]: ...


    @caas.service("datastore")
    class DataStoreIntercept:
        def put_item(self, key: str, value: Any) -> None: ...

        def get_item(self, key: str) -> None: ...

        def remove_item(self, key: str) -> None: ...

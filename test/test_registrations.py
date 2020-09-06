from typing import Any, List

import oaas
import unittest

from test.local_serialization_provider import LocalSerializationProvider
from oaas.serialization_provider import SerializationProvider


@oaas.service("datastore")
class DataStoreService:
    def __init__(self) -> None:
        self._items = dict()

    def put_item(self, key: str, value: Any) -> None:
        self._items[key] = value

    def get_item(self, key: str) -> Any:
        if key in self._items:
            return self._items.get(key)

        return None

    def remove_item(self, key: str) -> None:
        del self._items[key]


oaas.serve()


@oaas.client("datastore")
class DataStore:
    def put_item(self, key: str, value: Any) -> None:
        ...

    def get_item(self, key: str) -> None:
        ...

    def remove_item(self, key: str) -> None:
        ...


provider = LocalSerializationProvider()
oaas.register_serialization_provider(provider)

oaas.serve()


class TestServiceRegistrar(unittest.TestCase):
    def test_service_calls(self) -> None:
        data_store = oaas.get_client(DataStore)

        self.assertIsNone(data_store.get_item("a"))
        data_store.put_item("a", "avalue")
        self.assertEqual("avalue", data_store.get_item("a"))
        data_store.remove_item("a")
        self.assertIsNone(data_store.get_item("a"))

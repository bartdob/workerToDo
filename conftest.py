import pytest

from pytest_factoryboy import register
from tests.factories import WorkerFactory

register(WorkerFactory)

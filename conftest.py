import pytest

from chubbyfolio.test import Factory
from chubbyfolio.test import mixer as _mixer
from chubbyfolio.test.api_client import DRFClient

collect_ignore_glob = ['frontend/*']


@pytest.fixture
def factory(db):
    return Factory


@pytest.fixture
def mixer(db):
    return _mixer


@pytest.fixture
def api():
    return DRFClient()

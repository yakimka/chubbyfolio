import tempfile

import pytest

from chubbyfolio.test import Factory
from chubbyfolio.test import mixer as _mixer
from chubbyfolio.test.api_client import DRFClient

collect_ignore_glob = ['frontend/*']


@pytest.fixture
def override_media_root(settings):
    temp_dir = tempfile.mkdtemp(prefix='chubbyfolio_media')
    settings.MEDIA_ROOT = temp_dir
    return temp_dir


@pytest.fixture
def factory(db, override_media_root):
    return Factory


@pytest.fixture
def mixer(db, override_media_root):
    return _mixer


@pytest.fixture
def api():
    return DRFClient()

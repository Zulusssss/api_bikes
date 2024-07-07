import pytest
from django.conf import settings


@pytest.fixture(autouse=True)
def enable_celery_eager():
    settings.CELERY_TASK_ALWAYS_EAGER = True
    settings.CELERY_TASK_EAGER_PROPAGATES = True

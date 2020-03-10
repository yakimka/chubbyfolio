import pytest
from rest_framework.reverse import reverse

URL = reverse('feedback_message_create')


def test_empty_request_body(api):
    got = api.post(URL, expected_status_code=400)

    assert got == {'name': ['Это поле обязательно.'], 'phone': ['Это поле обязательно.']}


@pytest.mark.django_db
def test_create_message(api):
    got = api.post(URL, data={
        'name': 'Иван',
        'phone': '+381231234567',
        'text': 'take my money!',
    })

    assert got == {'name': 'Иван', 'phone': '381231234567', 'text': 'take my money!'}

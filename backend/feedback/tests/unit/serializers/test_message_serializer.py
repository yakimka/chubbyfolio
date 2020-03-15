import pytest

from feedback.api.serializers import MessageSerializer

serializer_cls = MessageSerializer


@pytest.mark.parametrize('data,expected', [
    ({}, 'required'),
    ({'name': '', 'phone': ''}, 'blank'),
])
def test_required(data, expected):
    serializer = serializer_cls(data=data)

    assert serializer.is_valid() is False
    assert serializer.errors['name'][0].code == expected
    assert serializer.errors['phone'][0].code == expected


@pytest.mark.parametrize('phone', [
    '1',
    '123',
    '1qwertyuiopa',
    '1234567890ff',
    '1qwertyuiopa2345',
])
def test_validate_phone_bad(phone):
    serializer = serializer_cls(data={
        'name': 'Иван',
        'phone': phone
    })

    assert serializer.is_valid() is False
    assert serializer.errors['phone'][0] == 'Номер телефона должен состоять из 12 цифр'
    assert serializer.errors['phone'][0].code == 'invalid'


@pytest.mark.parametrize('phone', [
    '123456789012',
    'a380931234567',
    '380931234567b',
    'a380931234567b',
])
def test_validate_phone_good(phone):
    serializer = serializer_cls(data={
        'name': 'Иван',
        'phone': phone
    })

    assert serializer.is_valid() is True
    assert bool(serializer.errors) is False

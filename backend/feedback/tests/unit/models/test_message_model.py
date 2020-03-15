def test_str(mixer):
    message = mixer.blend('feedback.Message')

    assert str(message) == f'{message.name} | {message.phone}'

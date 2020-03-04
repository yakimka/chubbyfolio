from django.apps import apps

from feedback.apps import FeedbackConfig


def test_feedback_config():
    assert FeedbackConfig.name == 'feedback'
    assert apps.get_app_config('feedback').name == 'feedback'

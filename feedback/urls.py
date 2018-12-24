from django.urls import path

from .api.views import CreateMessageView

urlpatterns = [
    path('message/', CreateMessageView.as_view(), name='feedback_message_create'),
]

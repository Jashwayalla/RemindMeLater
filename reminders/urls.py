from django.urls import path
from .views import ReminderListCreateView

urlpatterns = [
    path('reminders/', ReminderListCreateView.as_view(), name='reminder-list-create'),
]

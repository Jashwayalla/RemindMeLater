from django.db import models

class Reminder(models.Model):
    REMINDER_CHOICES = [
        ('email', 'Email'),
        ('sms', 'SMS'),
    ]

    message = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    remind_via = models.CharField(max_length=10, choices=REMINDER_CHOICES)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.message[:30]} at {self.date} {self.time} via {self.remind_via}"

from django.db import models
from django.utils import timezone
from company_users.time_stamped_model import TimeStampedModel

class CompanyUser(TimeStampedModel):
    Choices = [
        ('qa', 'QA'),
        ('developer', 'Developer'),
        ('manager', 'Manager'),
    ]
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    type = models.CharField(max_length=10, choices=Choices)
    date_joined = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

from django.db import models
from company_users.models import CompanyUser
from projects.models import Project
from django.utils import timezone
from company_users.time_stamped_model import TimeStampedModel

class Bug(TimeStampedModel):
    BUG_CHOICES = [
        ('pending', 'Pending'),
        ('inprogress', 'In Progress'),
        ('closed', 'Closed'),
    ]

    SCREENSHOT_CHOICES = [
        ('png', 'PNG'),
        ('gif', 'GIF'),
    ]
    title = models.CharField(max_length=255)
    description = models.TextField()
    screenshot_type = models.CharField(max_length=3, choices=SCREENSHOT_CHOICES, blank=True, null=True)
    bug_type = models.CharField(max_length=20, choices=BUG_CHOICES, default='pending')
    assignedproject = models.ForeignKey(
        Project, 
        on_delete=models.CASCADE,
        related_name='project_details'
    )
    assigneduser = models.ForeignKey(
        CompanyUser,
        on_delete=models.CASCADE,
        related_name='bug_user'
    )
     
    due_date = models.DateField(blank=True, default=timezone.now)
        
    def __str__(self):
        return self.title
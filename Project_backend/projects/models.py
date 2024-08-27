from django.db import models
from company_users.models import CompanyUser
from company_users.time_stamped_model import TimeStampedModel


class Project(TimeStampedModel):
    projectname = models.CharField(max_length=255)
    description = models.CharField(
        max_length=255, 
        null=True, 
        default="Redesign all the web pages with animation.",
        blank=True
    )
    manager = models.ForeignKey(
        CompanyUser, 
        on_delete=models.CASCADE,
        related_name='user_details',
    )
    image = models.ImageField(
        upload_to='project_images/', 
        null=True, 
        blank=True
    )
    def __str__(self):
        return self.projectname
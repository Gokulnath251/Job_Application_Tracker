from django.db import models

class JobApplication(models.Model):
    STATUS_CHOICES = [
        ('Applied', 'Applied'),
        ('Interview', 'Interview'),
        ('Selected', 'Selected'),
        ('Rejected', 'Rejected'),
    ]

    company_name = models.CharField(max_length=100)
    job_role = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    applied_date = models.DateField()
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Applied'
    )
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.company_name} - {self.job_role}"

# Create your models here.

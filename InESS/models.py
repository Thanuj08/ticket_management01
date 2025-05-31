from django.db import models
from django.contrib.auth.models import User

class Ticket(models.Model):
    # Priority options
    PRIORITY_CHOICES = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
        ('Critical', 'Critical'),
    ]

    # Department options
    DEPARTMENT_CHOICES = [
        ('Hardware', 'Hardware'),
        ('Software', 'Software'),
        ('Network', 'Network'),
        ('Other', 'Other'),
    ]

    # Ticket status options
    STATUS_CHOICES = [
        ('Open', 'Open'),
        ('In Progress', 'In Progress'),
        ('On Hold', 'On Hold'),
        ('Resolved', 'Resolved'),
        ('Closed', 'Closed'),
    ]

    # Ticket fields
    title = models.CharField(max_length=200)  # Short title of the issue
    description = models.TextField()          # Full details
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES)  # Priority level
    department = models.CharField(max_length=20, choices=DEPARTMENT_CHOICES)  # Department related to issue
    location = models.CharField(max_length=100)  # Where issue occurred
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)  # The user who raised the ticket
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Open')  # Ticket status
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when ticket was created
    updated_at = models.DateTimeField(auto_now=True)      # Timestamp when ticket was last updated

    def __str__(self):
        return f"#{self.id} {self.title} ({self.status})"

from django.db import models
from django.contrib.auth.models import User
# No settings import necessary here. Keep model definitions self-contained.


class Report(models.Model):
    CATEGORY_CHOICES = [
        ('garbage', 'Garbage'),
        ('water', 'Water Issue'),
        ('electricity', 'Electricity'),
        ('road', 'Road / Pothole'),
        ('other', 'Other'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    location = models.CharField(max_length=255)
    image = models.ImageField(upload_to='issue_images/', blank=True, null=True)
    status = models.CharField(max_length=20, default="Pending")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

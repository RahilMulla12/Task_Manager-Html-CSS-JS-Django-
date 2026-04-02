from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):

    ROLE_CHOICES = (
        ('customer','Customer'),
        ('support','Support'),
        ('supervisor','Supervisor')
    )

    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    
    
class Query(models.Model):

    STATUS_CHOICES = (
        ('pending','Pending'),
        ('assigned','Assigned'),
        ('in_progress','In Progress'),
        ('resolved','Resolved'),
        ('escalated','Escalated')
    )

    customer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="customer_queries"
    )

    assigned_to = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="assigned_queries"
    )

    message = models.TextField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="pending"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    assigned_at = models.DateTimeField(null=True, blank=True)
    
    
class QueryResponse(models.Model):

    query = models.ForeignKey(Query, on_delete=models.CASCADE)
    responder = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
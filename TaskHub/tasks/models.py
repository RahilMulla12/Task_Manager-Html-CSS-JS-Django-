from django.db import models
from user.models import User

class Task(models.Model):
    Status_Choice=(("pending", "Pending"),
        ("assigned", "Assigned"),
        ("in_progress", "In Progress"),
        ("submitted", "Submitted"),
        ("accepted", "Accepted"),
        ("revision_requested", "Revision Requested"),
    )
    
    title= models.CharField(max_length=200)
    discription = models.TextField( max_length=500)
    assigned_to = models.ForeignKey(User,on_delete= models.CASCADE,related_name="assigned_task")
    product_image = models.ImageField(upload_to="products/")
    created_by = models.ForeignKey(User,on_delete=models.CASCADE,related_name="created_task")
    status= models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.title

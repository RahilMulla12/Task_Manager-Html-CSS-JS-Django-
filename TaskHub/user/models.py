from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    Role_Choices=(
        ("admin","Admin"),
        ("user","User")
    )
    
    role= models.CharField(max_length=30,choices=Role_Choices,default="user")
    profile_image = models.ImageField(upload_to="profiles/",null=True,blank=True)
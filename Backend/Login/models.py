from click import password_option
from django.db import models

class Profile(models.Model) :
    login = False
    username = models.CharField(max_length=30)
    full_name = models.CharField(max_length=100)
    password = models.CharField(max_length=20)
    email = models.EmailField(max_length=254)
    is_student = models.BooleanField()
    is_staff = models.BooleanField()
    is_prof = models.BooleanField()
    def __str__(self):
        return self.username
    
    
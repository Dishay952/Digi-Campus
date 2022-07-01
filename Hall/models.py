from datetime import date
from time import time
from django.db import models
from django.contrib.auth.models import User

class hallPresence(models.Model):
    hall_numnber = models.IntegerField()
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    user_visiting=models.IntegerField(null=True)
    room_visiting = models.CharField(max_length=4,null=True)
    in_hall=models.BooleanField(default=False)
    laptop=models.BooleanField(default=False)
    timeEntered=models.DateTimeField(null=True)
    timeExit=models.DateTimeField(null=True)
    first_name=models.CharField(max_length=40,null=True)
    last_name=models.CharField(max_length=40,null=True)
    roll_no=models.IntegerField(null=True)
    mobile_no=models.BigIntegerField(null=True)
#  
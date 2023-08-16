from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth import get_user_model
from datetime import datetime 

now = datetime.now()
now.strftime("%y-%m-%d %H:%M:%S")
now=now.isoformat(' ','seconds')


class ValueModel(models.Model):
	input_values = models.CharField(max_length=255,blank=True)
	timestamp = models.DateTimeField(default= now,editable=False,null=True,blank=True)
	user=models.ForeignKey(get_user_model(),on_delete=models.CASCADE,null=True,blank=True)

	def __str__(self):
		return self.input_values + " by "+ str(self.timestamp)


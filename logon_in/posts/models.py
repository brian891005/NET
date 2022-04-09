from django.db import models
from django.utils import timezone
# Create your models here.
class Upload_Image(models.Model):
    user_name = models.CharField(max_length=30,default='brian')
    image = models.ImageField(upload_to='images/',blank =False , null =False)
    date = models.DateField(default=timezone.now)

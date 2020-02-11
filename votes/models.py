from django.db import models

# Create your models here.

class voters(models.Model):
    name=models.CharField(max_length=30)
    number=models.CharField(max_length=20)
    voted = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class videos(models.Model):
    id_name=models.CharField(max_length=10,default="")
    name=models.CharField(max_length=200,default="")
    votes=models.CharField(max_length=20,default="0")
    videofile=models.FileField(upload_to='videos/',null=True)

    def __str__(self):
        return self.name

from django.db import models

# Create your models here.
class Formation(models.Model):
    titer=models.CharField(max_length=30,null=True)
    logo=models.ImageField(upload_to = "images/",null=True)
    categ=models.CharField(max_length=20,null=True)
    etat=models.BooleanField(default=False,null=True)
    def __str__(self):
        return self.titer

from django.db import models

# Create your models here.
class students(models.Model):
    email=models.EmailField()
    name=models.CharField(max_length=50)
    mobile_number=models.IntegerField()
    city=models.CharField(max_length=30)
    referal_code=models.CharField(max_length=8,blank=True)
    referal_email=models.EmailField(blank=True)
    user_code=models.CharField(max_length=8,blank=True)
    password=models.CharField(max_length=255)
    def __str__(self):
        return f"{self.email}"
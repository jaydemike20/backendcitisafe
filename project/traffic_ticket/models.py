from django.db import models

# Create your models here.
class penalty(models.Model):


    description = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=9, decimal_places=2)
    status = models.CharField(max_length=50)
    date = models.DateField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.description
    


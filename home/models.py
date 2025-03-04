from django.db import models

# Create your models here.

class Car(models.Model):
    car_name=models.CharField(max_length=50)
    mileage=models.IntegerField()
    price=models.IntegerField()
    img=models.ImageField(upload_to='CarImages/')

    def __str__(self):
        return self.car_name
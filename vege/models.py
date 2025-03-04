from django.db import models
from django.contrib.auth.models import User


class recepies(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    recepie_name=models.CharField(max_length=100)
    recepie_description=models.TextField()
    recepie_img=models.ImageField(upload_to='CarImages')

    def __str__(self) -> str:
        return self.recepie_name

# class register(models.Model):
#     username=models.CharField(max_length=100)
#     email=models.EmailField()
#     password=models.CharField(max_length=100)

#     def __str__(self) -> str:
#         return self.username

    
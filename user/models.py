from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class CreateUser(AbstractUser):
    image = models.ImageField(upload_to='user_image/', blank=True, null=True)


    class Meta:
        db_table = 'create_user'



    def __str__(self):
        return self.username




from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from user.models import CreateUser

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey('user.CreateUser', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post_image/', blank=True, null=True)



    class Meta:
        db_table = 'post'


    def __str__(self):
        return self.title




class Review(models.Model):
    comment = models.CharField(max_length=200)
    star_given = models.IntegerField(
        default=0,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(0)
        ]
     )
    Post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(CreateUser, on_delete=models.CASCADE)

    class Meta:
        db_table ='review'

    def __str__(self):
        return f'{self.star_given} - {self.post.title} - {self.user.username}'



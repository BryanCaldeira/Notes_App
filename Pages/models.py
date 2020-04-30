from django.db import models



class Post(models.Model):
    user_email=models.CharField(max_length=50)

    def __str__(self):
    	return user_email

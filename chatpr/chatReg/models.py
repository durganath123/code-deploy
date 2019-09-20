from django.db import models

class DB(models.Model):
    username= models.CharField(max_length=100)
    msg=models.TextField()
    text=models.CharField(max_length=100)
    def __str__(self):
        return self.username

class Author(models.Model):
    name = models.CharField(max_length=100)
    username= models.CharField(max_length=100)
    msg=models.TextField()
    text=models.CharField(max_length=100)

    def __str__(self):
        self.username
        self.msg
        return self.name
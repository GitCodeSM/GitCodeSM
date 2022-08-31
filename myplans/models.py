
# Create your models here.
from tkinter import CASCADE
from django.db import models
from django.forms import CharField, DateTimeField

'''
Api: My plans - models: My user (for user name), Plans (plan options for user in table form)
'''
class MyUser(models.Model):
    full_name = models.CharField(default= 'yourname', max_length=100)
    
    def __str__(self):
        return self.full_name

class Plans(models.Model):
    default_userplan = models.CharField(default='100Rs', max_length=6)
    another_userplan = models.CharField(default='200Rs', max_length=6)
    theuser = models.ForeignKey(MyUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.default_userplan

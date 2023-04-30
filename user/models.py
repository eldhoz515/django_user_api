from django.db import models

class User():
    username=models.CharField()
    password=models.Field()
    email=models.Field()
    mobile = models.IntegerField()
    name = models.CharField()
    address = models.CharField()

    def __str__(self):
        return self.username
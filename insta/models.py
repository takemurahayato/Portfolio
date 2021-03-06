from django.db import models

class User(models.Model):
    name = models.CharField(max_length=50)
    mail = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.name + self.mail + self.password
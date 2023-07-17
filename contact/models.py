from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=110)
    email = models.EmailField()
    message = models.TextField()
    
    
    def __str__(self):
        return f"Message From{self.email}" 

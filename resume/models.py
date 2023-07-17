from django.db import models


class Skill(models.Model):
    title = models.CharField(max_length=110)
    percent = models.IntegerField(default=0)
    
    
    def __str__(self):
        return f'SKill:{self.title}-percent:{self.percent}'


class BaseResume(models.Model):
    title = models.CharField(max_length=110)
    date_range = models.CharField(max_length=50, help_text='Please Enter Date Rande In a String like 1990-2023  or 1990-Now')
    description = models.TextField()
    
    
    class Meta:
        abstract  = True
    
    def __str__(self):
        return self.title


class Experience(BaseResume):
    
    
    def __str__(self):
        return f"Experince:{self.title}"


class Education(BaseResume):
    
    
    def __str__(self):
        return f"Education:{self.title}"

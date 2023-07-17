from django.db import models
from .utils import upload_image_to_gallery
from django.urls import reverse_lazy


class Portfolio(models.Model):
    title = models.CharField(max_length=110)
    customer_name = models.CharField(max_length=110)
    date = models.DateField()
    image = models.ImageField(upload_to='portfolio/banners/')
    categories = models.ManyToManyField(to="Category", related_name='portfolio') 
    description = models.TextField() 
    slug = models.SlugField(blank=True, null=True, unique=True, allow_unicode=True, help_text='Please Empty This Filed has Complete Automatically')
    
    
    def __str__(self):
        return f"Portfolio For {self.customer_name}-Title:{self.title}"
    
    
    def get_absolute_url(self):
        return reverse_lazy("portfolio:portfolio_detail", args=[self.slug])
    


class Category(models.Model):
    title = models.CharField(max_length=110)
    
    
    def __str__(self):
        return f"Category:{self.title}"
    

class ImageGallery(models.Model):
    title = models.CharField(max_length=110)
    image = models.ImageField(upload_to=upload_image_to_gallery)
    portflio = models.ForeignKey(Portfolio, on_delete=models.CASCADE, related_name='images')
    
    
    def __str__(self):
        return f" Image  Gallery For {self.portflio.title}"
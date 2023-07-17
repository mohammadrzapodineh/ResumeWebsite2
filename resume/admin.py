from django.contrib import admin
from .models import Education, Skill, Experience

# Register your models here.

admin.site.register(Experience)
admin.site.register(Education)
admin.site.register(Skill)


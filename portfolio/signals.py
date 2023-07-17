from django.db.models.signals import pre_save
from .models import Portfolio
from django.utils.text import slugify
from django.dispatch import receiver


@receiver(sender=Portfolio, signal=pre_save)
def create_persian_slug(sender,  instance, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.title, allow_unicode=True)
        instance.save()
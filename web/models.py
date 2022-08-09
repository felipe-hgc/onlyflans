import uuid

from django.db import models

# Create your models here.
from django.forms import forms


class Flan(models.Model):
    flan_uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=64)
    description = models.TextField()
    image_url = models.URLField()
    slug = models.SlugField()
    is_private = models.BooleanField()
    is_new = models.BooleanField()


class ContactForm(models.Model):
    contact_form_uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    customer_email = models.EmailField()
    customer_name = models.CharField(max_length=64)
    message = models.TextField()

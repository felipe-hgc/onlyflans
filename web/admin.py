from django.contrib import admin

# Register your models here.
from web.models import Flan, ContactForm

admin.site.register(Flan)
admin.site.register(ContactForm)
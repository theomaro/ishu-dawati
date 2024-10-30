from django.contrib import admin
from .models import Centre, Ticket, Comment

# Register your models here.

admin.site.register(Centre)
admin.site.register(Ticket)
admin.site.register(Comment)

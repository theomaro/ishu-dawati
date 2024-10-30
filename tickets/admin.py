from django.contrib import admin
from .models import Centre, Ticket, Comment, ActivityLog

# Register your models here.

admin.site.register(Centre)
admin.site.register(Ticket)
admin.site.register(Comment)
admin.site.register(ActivityLog)

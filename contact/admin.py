from django.contrib import admin
from .models import Contact
# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display=('firstname', 'lastname', 'email', 'subject', 'message')
    list_display_links=('email',)
admin.site.register(Contact,ContactAdmin)
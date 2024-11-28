from django.contrib import admin

# Register your models here.

from .models import ProvisionUser

class ProvisionUserAdmin(admin.ModelAdmin):

    list_display = ('id','username')

    list_display_links = ('id','username')

admin.site.register(ProvisionUser, ProvisionUserAdmin)
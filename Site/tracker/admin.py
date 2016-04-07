from django.contrib import admin
from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    model = Profile
    list_display = ('name', 'startDate', 'endDate')
    prepopulated_fields = {'slug': ('name', 'startDate', 'endDate')}


admin.site.register(Profile, ProfileAdmin)


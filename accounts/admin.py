from django.contrib import admin
from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user','primary_school', 'olevel_school', 'alevel_school',)
    search_fields = ('user',)
    prepopulated_fields = {'slug': ('name','birth_date',)}
    ordering = ['created']

admin.site.register(Profile, ProfileAdmin)
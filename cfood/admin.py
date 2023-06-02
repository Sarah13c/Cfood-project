from django.contrib import admin

from .models import UserApp, Topic, Recipe

admin.site.register(UserApp)
admin.site.register(Recipe)
admin.site.register(Topic)

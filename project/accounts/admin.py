from django.contrib import admin
from accounts.models import User, Enforcer, Treasurer,  UserProfile


# Register your models here.

admin.site.register(User)
admin.site.register(UserProfile)


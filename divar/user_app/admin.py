from django.contrib.admin import ModelAdmin , register
from .models import UserAccount

@register(UserAccount)
class UserAccountAdmin(ModelAdmin):
    pass

# Register your models here.

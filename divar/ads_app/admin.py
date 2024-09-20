from django.contrib.admin import ModelAdmin , register
from .models import Ad , Category

@register(Ad)
class AdAdmin(ModelAdmin):
    pass

@register(Category)
class CategoryAdmin(ModelAdmin):
    pass

# Register your models here.

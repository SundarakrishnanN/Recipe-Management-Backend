from django.contrib import admin
from .models import Recipe

class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'is_veg', 'quantity')
    search_fields = ('name', 'user__username')
    list_filter = ('is_veg',)

admin.site.register(Recipe, RecipeAdmin)

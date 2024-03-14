from django.contrib import admin
from .models import productos

# Register your models here.

class ProductosAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'stock')
    search_fields = ('nombre', 'precio', 'stock')
    list_editable = ('precio', 'stock')
    list_display_links = ('nombre',)

admin.site.register(productos, ProductosAdmin)


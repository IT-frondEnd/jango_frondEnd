from django.contrib import admin



from django.contrib import admin
from .models import Category, Product

admin.site.register(Category)
admin.site.register(Product)

from django.contrib import admin
from .models import Book  # misol uchun model

class BookAdmin(admin.ModelAdmin):
    class Media:
        css = {
            'all': ('css/admin.css',)
        }

admin.site.register(Book, BookAdmin)  # ✅ TO‘G‘RI!

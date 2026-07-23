from django.contrib import admin
from core.models import Sample, Book, Branch, Inventory

# Register models so they're manageable from the Django admin site
admin.site.register(Sample)
admin.site.register(Book)
admin.site.register(Branch)
admin.site.register(Inventory)
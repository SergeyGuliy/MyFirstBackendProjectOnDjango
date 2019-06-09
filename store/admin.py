from django.contrib import admin
from store.models import *

admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Product)
admin.site.register(ParentCategory)
admin.site.register(CartItem)
admin.site.register(Cart)



# Register your models here.

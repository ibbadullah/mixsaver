from django.contrib import admin
from .models import *


# classes for making slugs
class BrandSlug(admin.ModelAdmin):
    prepopulated_fields = {'BrandSlug':('BrandName',)}

class CategoriesSlug(admin.ModelAdmin):
    prepopulated_fields = {'CategorySlug':('CategoryName',)}

class CouponProductSlug(admin.ModelAdmin):
    prepopulated_fields = {'CouponProductSlug':('CouponProductTitle',)}

# Register your models here.
admin.site.register(BrandsModel,BrandSlug)
admin.site.register(Categories,CategoriesSlug)
admin.site.register(CouponProducts,CouponProductSlug)



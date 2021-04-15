from django.contrib import admin

# Register your models here.
from spencersapp.models import Category

from spencersapp.models import SubCategory, DetailCategory

from spencersapp.models import Brand

from spencersapp.models import Products


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'MCName', 'LastmodifiedOn', 'created_at', 'IsActive', 'added_by', 'cat_image1')


admin.site.register(Category, CategoryAdmin)


class subCategoryAdmin(admin.ModelAdmin):
    list_display = ('MC', 'SCName')


admin.site.register(SubCategory, subCategoryAdmin)


class DetailCategoryAdmin(admin.ModelAdmin):
    list_display = ('SC', 'DCName')


admin.site.register(DetailCategory, DetailCategoryAdmin)


class BrandAdmin(admin.ModelAdmin):
    list_display = ('SC', 'DC', 'BName')


admin.site.register(Brand, BrandAdmin)


class ProductsAdmin(admin.ModelAdmin):
    list_display = (
    'MC', 'SC', 'DC', 'Brand', 'pname', 'slug', 'quantity', 'unit_quantity', 'batch_no', 'expiry_date', 'prod_desc',
    'mrp', 'total_price', 'landing_price', 'selling_price', 'offer_perc', 'offer_type', 'offer_from', 'offer_to',
    'image_tag1', 'image_tag2', 'image_tag3', 'image_tag4', 'offer_price', 'is_offer')


admin.site.register(Products, ProductsAdmin)

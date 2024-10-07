from django.contrib import admin

from .models import Product, ProductFoto, Category, SubCategory, ProposalNewCategory


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass

@admin.register(ProductFoto)
class ProductFoto(admin.ModelAdmin):
    pass

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(SubCategory)
class SubCategory(admin.ModelAdmin):
    pass


@admin.register(ProposalNewCategory)
class ProposalNewCategoryAdmin(admin.ModelAdmin):
    pass

from django.contrib import admin
import nested_admin
from .models import Section, Category, Product, ProductImage, \
                    Brand, DynamicProperty, DynamicPropertyValue, ProductVersion


class CategoryInline(admin.TabularInline):
    model = Category
    extra = 1


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ('title',)
    inlines = [CategoryInline]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'section', )


class ProductImageInline(nested_admin.NestedTabularInline):
    model = ProductImage
    extra = 1


class DynamicPropertyValueInline(nested_admin.NestedTabularInline):
    model = DynamicPropertyValue
    extra = 1


class ProductVersionInline(nested_admin.NestedTabularInline):
    model = ProductVersion
    extra = 1
    inlines = [DynamicPropertyValueInline]


@admin.register(DynamicProperty)
class DynamicPropertyAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(Product)
class ProductAdmin(nested_admin.NestedModelAdmin):
    inlines = [ProductImageInline, ProductVersionInline]


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('title', )




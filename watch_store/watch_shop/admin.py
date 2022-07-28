from django.contrib import admin
from .models import Brand, SubBrand, Product, ImagesProduct


class ImagesProductAdmin(admin.StackedInline):
    model = ImagesProduct


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('slug_brand', 'title_brand', 'created_brand_at', 'updated_brand_at', 'hidden_brand')
    list_display_links = ('slug_brand', 'title_brand')
    search_fields = ('title_brand', 'description_brand')
    list_editable = ('hidden_brand',)
    list_filter = ('hidden_brand', )

    prepopulated_fields = {'slug_brand': ('title_brand',)}


@admin.register(SubBrand)
class SubBrandAdmin(admin.ModelAdmin):
    list_display = ('slug_subbrand', 'title_subbrand', 'created_subbrand_at', 'updated_subbrand_at', 'hidden_subbrand',
                    'brand')
    list_display_links = ('slug_subbrand', 'title_subbrand')
    search_fields = ('title_subbrand', 'description_subbrand')
    list_editable = ('hidden_subbrand',)
    list_filter = ('hidden_subbrand', 'brand')

    prepopulated_fields = {'slug_subbrand': ('title_subbrand',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('vendor_code', 'title_product', 'created_product_at', 'updated_product_at', 'price_product',
                    'hidden_product', 'brand', 'subbrand')
    list_display_links = ('vendor_code', 'title_product')
    search_fields = ('vendor_code', 'title_product', 'description_product')
    list_editable = ('hidden_product',)
    list_filter = ('hidden_product', 'brand', 'subbrand', 'price_product')

    prepopulated_fields = {'vendor_code': ('title_product',)}
    inlines = [ImagesProductAdmin]

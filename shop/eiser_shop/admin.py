from django.contrib import admin

from eiser_shop import models

@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [ "title", "price"]
    # prepopulated_fields = {'slug': ('title', 'category'), }
    # inlines = [RecipeInline]
    save_as = True
    save_on_top = True

    # admin.site.register(models.BrowseCategories)
    # admin.site.register(models.ProductBrand)
    # admin.site.register(models.Color)
    # admin.site.register(models.Category)
    # admin.site.register(models.Coupon)
    # admin.site.register(models.Specification)
    # admin.site.register(models.CollectionBanner)
    # admin.site.register(models.informationblock)





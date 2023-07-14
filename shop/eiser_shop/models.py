from audioop import reverse
from django.db import models
from ckeditor.fields import RichTextField

# forms registration


class Category(models.Model):
    name = models.CharField(max_length=100, default="")
    slug = models.SlugField(max_length=200, default="")

    

    def __str__(self):
        return self.name
    
class informationblock(models.Model):
    icon = models.ImageField(blank=True, upload_to='icon banner' )
    title = models.CharField(max_length=100, default="") 
    text = models.CharField(max_length=100, default="")
    

    def __str__(self):
        return self.title

class CollectionBanner(models.Model):
    title = models.CharField(max_length=100, default="")
    image = models.ImageField(upload_to='collection')
    buttontext = models.CharField(max_length=30, default="")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    discount =  models.CharField(max_length=100, default="", blank=True)
    



    def __str__(self):
        return self.title

class BrowseCategories(models.Model):
    name = models.CharField(max_length=100, default="")
    
    def __str__(self):
        return self.name

class ProductBrand(models.Model):
    name = models.CharField(max_length=100, default="")

    def __str__(self):
        return self.name
    
class Color(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
# class Price(models.Model):
#     price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
#     discountprice = models.DecimalField(max_digits=10, decimal_places=2, default=0)

class Coupon(models.Model):
    code = models.CharField(max_length=50)
    discount = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.code



class Specification(models.Model):
    name = models.CharField(max_length=100, default="")
    meaning = models.CharField(max_length=100, default="")


    def __str__(self):
        return self.name

class Product(models.Model):
    title = models.CharField(max_length=100, default="")
    Images = models.ImageField(upload_to="product")
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    pricewithoutdiscount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    description = RichTextField(default="")
    availibility = models.CharField(max_length=100, default="")
    miniText = RichTextField(default="")
    browsecategories = models.ForeignKey(BrowseCategories, related_name='BrowseCategories', on_delete=models.SET_NULL, null=True, blank=True)
    productbrand = models.ForeignKey(ProductBrand, related_name='ProductBrand', on_delete=models.SET_NULL, null=True, blank=True)
    color = models.ManyToManyField(Color, related_name='Color', blank=True)
    category = models.ForeignKey(Category, related_name="product",  on_delete=models.SET_NULL,  null=True, 
                                 blank=True)
    slug = models.SlugField(max_length=300, default="")

    def get_absolute_url(self):
        return reverse('product', kwargs={'product_slug': self.slug})
    
    def __str__(self):
        return self.title
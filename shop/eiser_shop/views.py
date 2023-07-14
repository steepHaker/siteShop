from django.db.models import Q
from django.views.generic import ListView, DetailView
from django.shortcuts import  render
from .models import  BrowseCategories, CollectionBanner, Color, Product, Category, ProductBrand, informationblock


class HomeView(ListView):
    model = Product
    paginate_by = 3
    template_name = "eister_shop/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products_all'] = Product.objects.all()
        context['collection_banners'] = CollectionBanner.objects.all()[:1]
        context['information_blocks'] = informationblock.objects.all()
        context['products'] = Product.objects.all()[:3]
        return context

class ProductView(ListView):
    model = Product
    template_name = "eister_shop/product.html"
    context_object_name = 'product_info'
    slug_url_kwarg = 'post_slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products_info'] = Product.objects.all()
        context['browse_categories'] = BrowseCategories.objects.all()
        context['brands'] = ProductBrand.objects.all()
        context['productcolors'] = Color.objects.all()
        context['category_name'] = Category.objects.all()
        return context
    
    def get_queryset(self):
        queryset = super().get_queryset()

        category = self.request.GET.get('category')
        brand = self.request.GET.get('brand')
        color = self.request.GET.get('color')
        min_price = self.request.GET.get('min_price')
        max_price = self.request.GET.get('max_price')

        filters = Q()

        if category:
            filters &= Q(browsecategories__name=category)
        if brand:
            filters &= Q(productbrand__name=brand)
        if color:
            filters &= Q(color__name=color)
        if min_price:
            filters &= Q(price__gte=min_price)
        if max_price:
            filters &= Q(price__lte=max_price)

        queryset = queryset.filter(filters)

        return queryset
    
class ProductDetailView(DetailView):
    model = Product
    slug_url_kwarg = 'product_slug'
    template_name = 'eister_shop/include/product_info.html'

class FilteredProductView(ListView):
    model = Product
    template_name = "eister_shop/filtered_product.html"
    context_object_name = 'filtered_products'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()

        category = self.request.GET.get('category')
        brand = self.request.GET.get('brand')
        color = self.request.GET.get('color')
        min_price = self.request.GET.get('min_price')
        max_price = self.request.GET.get('max_price')

        filters = Q()

        if category:
            filters &= Q(category__name=category)
        if brand:
            filters &= Q(productbrand__name=brand)
        if color:
            filters &= Q(color__name=color)
        if min_price:
            filters &= Q(price__gte=min_price)
        if max_price:
            filters &= Q(price__lte=max_price)

        queryset = queryset.filter(filters)

        return queryset

class OrderTrackingView(DetailView):
    model = Product
    paginate_by = 3
    template_name = "eister_shop/order_tracking.html"

    def get(self, request):
        order_trackings = Product.objects.all()
        return render(request, 'eister_shop/order_tracking.html', {"order_tracking": order_trackings})


class ContactView(ListView):
    model = CollectionBanner
    paginate_by = 3
    template_name = "eister_shop/contact.html"

    def get(self, request):
        contacts = CollectionBanner.objects.all()
        return render(request, 'eister_shop/contact.html', {"contact": contacts})
    
  
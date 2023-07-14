from django.urls import path
from eiser_shop.views import HomeView, ProductView,  ProductDetailView #CardView,
from eiser_shop.views import FilteredProductView, OrderTrackingView, ContactView


urlpatterns =[ 
    path('', HomeView.as_view(), name='home'),
    path('product/', ProductView.as_view(), name='product'),
    path('product/<slug:product_slug>/', ProductDetailView.as_view(), name='product'),
    # path('gift-card/', CardView.as_view(), name='gift-card'),
    
    path('order_tracking/', OrderTrackingView.as_view(), name='order_tracking'),
    path('filtered-product/', FilteredProductView.as_view(), name='filtered_product'),
]
   

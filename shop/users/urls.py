from django.urls import include, path
from eiser_shop.views import ContactView

from users.views import CardView, CreateAссaunt, AddToFavoritesView #CheckOutView

urlpatterns = [
    path('gift-card/', CardView.as_view(), name='gift-card'),
    path('checkout/', CreateAссaunt.as_view(), name='checkout'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('add-to-favorites/<int:product_id>/', AddToFavoritesView.as_view(), name='add_to_favorites'),
    path('my-card/', CardView.as_view(), name='card'),
]
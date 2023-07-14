from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import View, DetailView, CreateView, TemplateView
from eiser_shop.models import Product
from users.forms import ContactForm
from .models import Card, User
from django.views.decorators.csrf import csrf_exempt




# @csrf_exempt
# def AddToFavoritesView(request, product_id):
#     if request.method == 'POST':
#         product = Product.objects.get(pk=product_id)
#         cart = Card.objects.get(user=request.user)
#         cart.products.add(product)
#         return JsonResponse({"message": "Продукт успешно добавлен в избранное"})
#     else:
#         return JsonResponse({"message": "Invalid request method"})

        
# class CardView(TemplateView):
#     model = Product
#     paginate_by = 3
#     template_name = "eister_shop/card.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['products'] = Product.objects.all()
#         return context

#     def get(self, request):
#         products = Product.objects.all()
#         return render(request, 'eister_shop/card.html', {"card": products})



class AddToFavoritesView(View):
    def post(self, request, product_id):
        product = get_object_or_404(Product, pk=product_id)
        cart, _ = Card.objects.get_or_create(user=request.user)
        cart.products.add(product)
        return JsonResponse({"message": "Продукт успешно добавлен в избранное"})

class CardView( TemplateView):
    model = Product
    paginate_by = 3
    template_name = "eister_shop/card.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.all()
        return context

    def get(self, request):
        cart = Card.objects.get(user=request.user)  # Добавлено: получаем корзину только для аутентифицированных пользователей
        products = cart.products.all()
        return render(request, 'eister_shop/card.html', {"card": products})


































    


    

# страница входа
class CheckOutView(DetailView):
    model = Product
    paginate_by = 3
    template_name = "registration/checkout.html"

    def get(self, request):
        checkoutView = Product.objects.all()
        return render(request, 'registration/checkout.html', {"checkoutView": checkoutView})
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = User()
        return context        



































    


class CreateAссaunt(CreateView):
    model = User
    form_class = ContactForm
    template_name = 'registration/login.html'  # указываете имя вашего шаблона для регистрации

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            
            self.object = form.save()
            return render(request, 'eister_shop/home.html')  # указываете имя вашего шаблона для успешной регистрации
        else:
            return render(request, self.template_name, {'form': form})
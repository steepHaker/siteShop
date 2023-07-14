# from django import template
# from eiser_shop.models import Category, MenuItem, Product

# register = template.Library()

# def get_menu_item():
#     return MenuItem.objects.all()

# @register.simple_tag()
# def get_list_item():
#     return get_menu_item

# @register.inclusion_tag('eister_shop/include/tags/top_menu.html')
# def get_list():
#     menu_items = get_menu_item()
#     return {"list_item": menu_items}



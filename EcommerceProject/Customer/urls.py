from django.urls import path
from .views import Cartview, Customergroceryview, Customerlaptopview, Customermobileview, Deleteitemview, Groceryview, HomeView, Laptopview, Mobileview, Updateallitemview



urlpatterns=[
    path('home/',HomeView,name='customerhome'),
    path('customermobile/',Customermobileview,name='customermobile'),
    path('customerlaptop/',Customerlaptopview,name='customerlaptop'),
    path('customergrocery/',Customergroceryview,name='customergrocery'),
    path('customerorderitem/<int:pk>',Laptopview,name='customerorderitem'),
    path('customermobileitem/<int:pk>',Mobileview,name='customermobileitem'),
    path('customergroceryitem/<int:pk>',Groceryview,name='customergroceryitem'),
    path('cartview/',Cartview,name='cartview'),
    path('deleteitem/<int:pk>',Deleteitemview,name='deleteitem'),
    path('customerupdateitem/<int:pk>',Updateallitemview,name='customerupdateitem'),

]
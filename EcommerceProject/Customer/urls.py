from django.urls import path
from .views import Cartview, Customerorderlistview, Customerordersview, Deleteitemview, Groceryview, HomeView, Laptopview, Mobileview,Updateallitemview,showMobile,showlaptop,showGrocery



urlpatterns=[
    path('home/',HomeView,name='customerhome'),
    # path('customermobile/',Customermobileview,name='customermobile'),
    # path('customerlaptop/',Customerlaptopview,name='customerlaptop'),
    # path('customergrocery/',Customergroceryview,name='customergrocery'),
    path('showlaptop/',showlaptop, name='showlaptop'),
    path('showmobile/',showMobile, name='showmobile'),
    path('showgrocery/',showGrocery, name='showgrocery'),
    
    path('customerlaptopitem/<int:pk>',Laptopview,name='customerlaptopitem'),
    path('customermobileitem/<int:pk>',Mobileview,name='customermobileitem'),
    path('customergroceryitem/<int:pk>',Groceryview,name='customergroceryitem'),
    path('cartview/',Cartview,name='cartview'),
    path('deleteitem/<int:pk>',Deleteitemview,name='deleteitem'),
    path('customerupdateitem/<int:pk>',Updateallitemview,name='customerupdateitem'),
    path('customerorder/',Customerordersview,name='customerorder'),
    path('customerorderlist/',Customerorderlistview,name='customerorderlist')


]

# path('customerlaptopitem/<int:pk>',Laptopview,name='customerlaptopitem'),
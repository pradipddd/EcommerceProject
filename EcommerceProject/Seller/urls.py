from django.urls import path
from .views import ProductView, Sellergrocerydeleteview, Sellergroceryupdateview, Sellergroceryview, Sellerhomeview, Sellerinventoryview, Sellerlaptopdeleteview, Sellerlaptopupdateview, Sellerlaptopview, Sellermobiledeleteview, Sellermobileupdateview, Sellermobileview



urlpatterns=[
    path('sellerhome/',Sellerhomeview,name='sellerhome'),
    path('sellerproduct/',ProductView,name='sellerproduct'),
    path('sellerlaptop/',Sellerlaptopview,name='sellerlaptop'),
    path('sellermobile/',Sellermobileview,name='sellermobile'),
    path('sellergrocery/',Sellergroceryview,name='sellergrocery'),
    path('sellerinventory/',Sellerinventoryview,name='sellerinventory'),
    path('sellerlaptopupdate/<int:lapupdate>',Sellerlaptopupdateview,name='sellerlaptopupdate'),
    path('sellermobileupdate/<int:mobupdate>',Sellermobileupdateview,name='sellermobileupdate'),
    path('sellergroceryupdate/<int:groupdate>',Sellergroceryupdateview,name='sellergroceryupdate'),
    path('sellerlaptopdelete/<int:lapdelete>',Sellerlaptopdeleteview,name='sellerlaptopdelete'),
    path('sellermobiledelete/<int:mobdelete>',Sellermobiledeleteview,name='sellermobiledelete'),
    path('sellergrocerydelete/<int:grodelete>',Sellergrocerydeleteview,name='sellergrocerydelete'),
    
]
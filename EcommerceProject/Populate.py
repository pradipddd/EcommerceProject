import os 
os.environ.setdefault('DJANGO_SETTINGS_MODULE','EcommerceProject.settings')
import django
django.setup()
from Seller.models import *
from faker import Faker
from random import *
fake=Faker()



def Populatelaptop(x):
        product=Product.objects.get(id=2)
        for i in range(x):
            fproduct=choices([product])
            fbrand_name=choices(['HP','SONY','DELL','LENOVO','ASUS','APPLE'])
            fmodel_name=choices(['Envy15','VivoA54','Inspiron15','Elite Book','MacBook Air','AlienwareS3'])
            fram=choices([4,6,8,16])
            f_rom=choices([256,500,1000])
            fprocessor=choices(['i5','i3','i7','i9','Ryzen'])
            fprice=randint(40000,150000)
            fquantity=randint(1,50)
            fwarranty=choices([6,12,24,36])
            flimage=choices(['Laptops/mac.jpg','Laptops/mac2.jpg','Laptops/al1.jpg','Laptops/al2.jpg'])
            lap_record=Laptop.objects.get_or_create(product=fproduct[0],brand_name=fbrand_name[0],model_name=fmodel_name[0],ram=fram[0],rom=f_rom[0],processor=fprocessor[0],price=fprice,quantity=fquantity,warranty=fwarranty[0],limage=flimage[0])
        print('Data Inserted!!')
Populatelaptop(10)

def Populatemobile(x):
        product=Product.objects.get(id=1)
        for i in range(x):
            fproduct=choices([product])
            fbrand_name=choices(['Apple','Samsung','Vivo','Realme','MI','OnePlus'])
            fmodel_name=choices(['Iphone13','VivoA54','Realme GT','OnePlus 9pro','Redmi Note10','S30 Zplus'])
            fram=choices([4,6,8,12])
            f_rom=choices([64,128,256])
            fprocessor=choices(['Mediatek G96','Snapdragon 660','Bionic A15','ExynosA8','Snapdragon 888'])
            fprice=randint(20000,100000)
            fquantity=randint(1,100)
            fwarranty=choices([6,12])
            fmimage=choices(['Mobiles/ma1.jpg','Mobiles/ma2.jpg','Mobiles/mo1.jpg','Mobiles/mo2.jpg','Mobiles/mv1.jpg','Mobiles/mv2.jpg'])
            mob_record=Mobile.objects.get_or_create(product=fproduct[0],brand_name=fbrand_name[0],model_name=fmodel_name[0],ram=fram[0],rom=f_rom[0],processor=fprocessor[0],price=fprice,quantity=fquantity,warranty=fwarranty[0],mimage=fmimage[0])
        print('Data Inserted!!')
Populatemobile(10)

def Populategrocery(x):
        product=Product.objects.get(id=3)
        for i in range(x):
            fproduct=choices([product])
            fproduct_name=choices(['Maggie','Nutela','LifeBoy Soap','Almond Oil','Virgin Oil','Tomato Ketchep'])
            fprice=randint(40,400)
            fquantity=randint(1,100)
            fwarranty=choices([3,6,12])
            fgimage=choices(['Grocerys/gt1.jpg','Grocerys/gt2.jpg','Grocerys/gt3.jpg','Grocerys/gt4.jpg','Grocerys/gt5.png','Grocerys/gt6.jpg'])
            gro_record=Grocery.objects.get_or_create(product=fproduct[0],product_name=fproduct_name[0],price=fprice,quantity=fquantity,warranty=fwarranty[0],gimage=fgimage[0])
        print('Data Inserted!!')
Populategrocery(10)

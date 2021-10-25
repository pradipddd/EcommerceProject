from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from Seller.models import Laptop,Mobile,Grocery
from django.db.models import Q


def Search(request):
    if request.method == 'POST':
        search=request.POST.get('search')
        search1=search.capitalize()
        searchsplit=search.split(' ')
        if search1 == 'Laptop':
            laptop=Laptop.objects.all()
            print(laptop)
            print('')
            template_name='UniversalSearch/Universalsearch.html'
            context={'laptop':laptop}
            return render(request,template_name,context)
        elif search1 == 'Mobile':
            mobile=Mobile.objects.all()
            print(mobile)
            print('')
            template_name='UniversalSearch/Universalsearch.html'
            context={'mobile':mobile}
            return render(request,template_name,context)
        elif search1 == 'Grocery':
            grocery=Grocery.objects.all()
            print(grocery)
            print('')
            template_name='UniversalSearch/Universalsearch.html'
            context={'grocery':grocery}
            return render(request,template_name,context)
        else:
            laplist=[]
            for i in searchsplit:
                lap=Laptop.objects.filter(Q(model_name__icontains=i)|Q(brand_name__icontains=i)|Q(ram__icontains=i)|Q(rom__icontains=i)|Q(processor__icontains=i))
                laplist.extend(lap)
            lapset=set(laplist)
            print(lapset)
            moblist=[]
            for i in searchsplit:
                mob=Mobile.objects.filter(Q(model_name__icontains=i)|Q(brand_name__icontains=i)|Q(ram__icontains=i)|Q(rom__icontains=i)|Q(processor__icontains=i))
                moblist.extend(mob)
            mobset=set(moblist)
            print(mobset)
            grolist=[]
            for i in searchsplit:
                gro=Grocery.objects.filter(Q(product_name__icontains=i)|Q(price__icontains=i))
                grolist.extend(gro)
            groset=set(grolist)
            print(groset)
            if bool(lapset or mobset or groset)==False:
                blank='Record is not Found!!!!!!!'
                
                template_name='UniversalSearch/Universalsearch.html'
                context={'blank':blank}
                return render(request,template_name,context)
            else:
                print('else')
                template_name='UniversalSearch/Universalsearch.html'
                context={'lapset':lapset,'mobset':mobset,'groset':groset}
                return render(request,template_name,context)
    template_name='UniversalSearch/Universalsearch.html'
    context={}
    return render(request,template_name,context)
    





    



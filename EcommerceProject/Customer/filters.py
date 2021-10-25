import django_filters
from Seller.models import Laptop, Mobile, Grocery
from django import forms

class LaptopFilter(django_filters.FilterSet):
    # price = django_filters.NumberFilter()
    price__gt = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    price__lt = django_filters.NumberFilter(field_name='price', lookup_expr='lte')
    # price=django_filters.NumberFilter(lookup_expr='lte')
    # max_price=django_filters.NumberFilter(name='price',lookup_expr='lte')
    class Meta:
        model = Laptop
        fields = '__all__'
        exclude = ['limage', 'seller', 'stock','warranty','price','product']


class MobileFilter(django_filters.FilterSet):
    # price = django_filters.NumberFilter()
    price__gt = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    price__lt = django_filters.NumberFilter(field_name='price', lookup_expr='lte')
    # price=django_filters.NumberFilter(lookup_expr='lte')
    # price=django_filters.NumberFilter(lookup_expr='gte')
    class Meta:
        model = Mobile
        fields = '__all__'
        exclude = ['mimage', 'seller', 'stock','warranty','price','product']

        labels = {'name': 'Model Name',
                  'ram': 'RAM in GB',
                  'rom': 'RAM in GB',
                  'warranty': 'Warranty in months',
                  'price': 'Price in Rs.',
                  }
        widgets = {'ram': forms.TextInput(attrs={'placeholder': 'Ex. 2, 4, 8, 16, 32, 64....', }),
                   'rom': forms.TextInput(attrs={'placeholder': 'Ex. 16, 32, 64, 128, 256, 512, 1025... '}),
                   'processor': forms.TextInput(attrs={'placeholder': 'Ex. Octacore, DualCore '})}
                   


class GroceryFilter(django_filters.FilterSet):
    # price = django_filters.NumberFilter()
    price__gt = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    price__lt = django_filters.NumberFilter(field_name='price', lookup_expr='lte')
    # price=django_filters.NumberFilter(lookup_expr='lte')
    # max_price=django_filters.NumberFilter(name='price',lookup_expr='lte')
    class Meta:
        model = Grocery
        fields = '__all__'
        exclude = ['gimage', 'seller', 'stock','warranty','price','product']
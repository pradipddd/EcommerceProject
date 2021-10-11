from django.contrib import admin
from .models import Address, Country, State, City

class CountryAdmin(admin.ModelAdmin):
    list_display = ['id', 'country_name']
admin.site.register(Country, CountryAdmin)


class StateAdmin(admin.ModelAdmin):
    list_display = ['id', 'state_name']
admin.site.register(State, StateAdmin)


class CityAdmin(admin.ModelAdmin):
    list_display = ['id', 'city_name']
admin.site.register(City, CityAdmin)

class CustomerProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer','fname','lname','country','state','city','mobile','address','address_type']
admin.site.register(Address, CustomerProfileAdmin)


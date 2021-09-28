from django.contrib import admin
from .models import *


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')


admin.site.register(Category, CategoryAdmin)


class RegionAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')


admin.site.register(Region, RegionAdmin)


class ListingsAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'address', 'phone',
                    'category', 'region', 'date_posted')


admin.site.register(Listings, ListingsAdmin)


class PropertyAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'seller', 'rooms', 'bedrooms', 'bathrooms',
                    'sqfts', 'price', 'price_units', 'category', 'region', 'short_description', 'description', 'featured', 'date_posted')


admin.site.register(Property, PropertyAdmin)


class ContactsAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'address', 'phone',
                    'message', 'date_posted')


admin.site.register(Contact, ContactsAdmin)


class BookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone',
                    'location', 'propert', 'date_posted')


admin.site.register(Booking, BookingAdmin)

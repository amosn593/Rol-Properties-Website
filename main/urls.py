from django.urls import path
from .views import *

app_name = 'main'

urlpatterns = [
    path('', index, name='index'),
    path('properties/<str:slug>/', detailedview, name='detailedview'),
    path('property-view-booking/', booking, name='booking'),
    path('property-for-rent/', rent, name='rent'),
    path('property-for-sale/', sale, name='sale'),
    path('land-for-sale/', land, name='land'),
    path('contact-us/', contact, name='contact'),
    path('about-us/', about, name='about'),
    path('list-your-property/', listing, name='listing'),
    path('properties-search/', search, name='search'),
]

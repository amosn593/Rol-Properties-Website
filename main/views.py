from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import *

# Create your views here.


def index(request):
    if request.method == "GET":
        # try:
        posts = Property.objects.all()[:6]
        slides = Property.objects.filter(featured=True)[:3]
        context = {
            "posts": posts,
            "slides": slides,
        }
        return render(request, 'main/nav/home.html', context)
        # except:
        #     messages.error(
        #         request, 'Something went wrong, kindly try again!!!')
        #     return redirect("main:index")
    elif request.method == "POST":
        return HttpResponse("Invalid URL")
    else:
        return HttpResponse("Invalid URL")


def detailedview(request, slug):
    if request.method == "GET":
        try:
            post = Property.objects.get(slug=slug)
            context = {
                "post": post,
            }

            return render(request, 'main/incl/details.html', context)
        except:
            messages.error(
                request, 'Something went wrong, kindly try again!!!')
            return redirect("main:index")

    else:
        return HttpResponse("Invalid URL")


def booking(request):
    if request.method == "POST":
        name = request.POST["name"].strip()
        phone = request.POST["phone"].strip()
        email = request.POST["email"].strip()
        location = request.POST["location"].strip()
        id = request.POST["id"].strip()
        propert = Property.objects.get(id=int(id))
        try:
            b = Booking(name=name, phone=phone, email=email,
                        location=location, propert=propert)
            b.save()
            messages.success(
                request, 'Booking successfully!')
            return redirect("main:index")
        except:
            messages.error(
                request, 'Something went wrong, kindly try again!!!')
            return redirect("main:index")
    else:
        return HttpResponse("Invalid URL")


def rent(request):
    if request.method == "GET":
        try:
            posts = Property.objects.filter(
                category__name__icontains="rent")[:6]
            context = {
                "posts": posts,
            }
            return render(request, 'main/nav/rent.html', context)
        except:
            messages.error(
                request, 'Something went wrong, kindly try again!!!')
            return redirect("main:index")
    elif request.method == "POST":
        return HttpResponse("Invalid URL")
    else:
        return HttpResponse("Invalid URL")


def sale(request):
    if request.method == "GET":
        try:
            posts = Property.objects.filter(
                category__name__icontains="sale")[:6]
            context = {
                "posts": posts,
            }
            return render(request, 'main/nav/sale.html', context)
        except:
            messages.error(
                request, 'Something went wrong, kindly try again!!!')
            return redirect("main:index")
    elif request.method == "POST":
        return HttpResponse("Invalid URL")
    else:
        return HttpResponse("Invalid URL")


def land(request):
    if request.method == "GET":
        try:
            posts = Property.objects.filter(
                category__name__icontains="sale")[:6]
            context = {
                "posts": posts,
            }
            return render(request, 'main/nav/land.html', context)
        except:
            messages.error(
                request, 'Something went wrong, kindly try again!!!')
            return redirect("main:index")
    elif request.method == "POST":
        return HttpResponse("Invalid URL")
    else:
        return HttpResponse("Invalid URL")


def contact(request):
    if request.method == "GET":
        return render(request, 'main/nav/contact.html')
    elif request.method == "POST":
        name = request.POST["name"].strip()
        phone = request.POST["phone"].strip()
        email = request.POST["email"].strip()
        address = request.POST["address"].strip()
        message = request.POST["message"].strip()
        try:
            c = Contact(name=name, phone=phone, email=email,
                        address=address, message=message)
            c.save()
            messages.success(
                request, 'Your message sent successfully!')
            return redirect("main:index")
        except:
            messages.error(
                request, 'Something went wrong, kindly try again!!!')
            return redirect("main:index")
    else:
        return HttpResponse("Invalid URL")


def about(request):
    if request.method == "GET":
        return render(request, 'main/nav/about.html')
    elif request.method == "POST":
        return HttpResponse("Invalid URL")
    else:
        return HttpResponse("Invalid URL")


def listing(request):
    if request.method == "GET":
        return render(request, 'main/forms/listing.html')
    elif request.method == "POST":
        name = request.POST["name"].strip()
        phone = request.POST["phone"].strip()
        email = request.POST["email"].strip()
        address = request.POST["address"].strip()
        region = request.POST["region"].strip()
        category = request.POST["property"].strip()
        try:
            l = Listings(name=name, phone=phone, email=email,
                         address=address, region=region, category=category)
            l.save()
            messages.success(
                request, 'Your message sent successfully!')
            return redirect("main:index")
        except:
            messages.error(
                request, 'Something went wrong, kindly try again!!!')
            return redirect("main:index")
    else:
        return HttpResponse("Invalid URL")


def search(request):
    if request.method == "POST":
        keyword = request.POST["keyword"].strip()
        region = request.POST["region"].strip()
        category = request.POST["category"].strip()
        max_price = request.POST["max_price"].strip()

        try:
            posts = Property.objects.filter(
                name__icontains=keyword, region__name__icontains=region, category__name__icontains=category)[:12]
            num = posts.count()
            context = {
                "posts": posts,
                "num": num,
            }
            return render(request, 'main/nav/searchResults.html', context)
        except:
            messages.error(
                request, 'Something went wrong, kindly try again!!!')
            return redirect("main:index")
    else:
        return HttpResponse("Invalid URL")

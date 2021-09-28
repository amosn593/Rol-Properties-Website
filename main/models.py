from django.db import models
from autoslug import AutoSlugField


class Category(models.Model):
    name = models.CharField(max_length=30, unique=True)
    slug = AutoSlugField(populate_from='name')

    class Meta:
        ordering = ('-id',)

    def __str__(self):
        return self.name


class Region(models.Model):
    name = models.CharField(max_length=30, unique=True)
    slug = AutoSlugField(populate_from='name')

    class Meta:
        ordering = ('-id',)

    def __str__(self):
        return self.name


class Listings(models.Model):
    name = models.CharField(max_length=30)
    slug = AutoSlugField(populate_from='name')
    email = models.EmailField(max_length=30)
    address = models.CharField(max_length=30)
    phone = models.CharField(max_length=15)
    category = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    date_posted = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ('-id',)

    def __str__(self):
        return self.name


CATEGORIES = (
    ("Sale", "Sale"),
    ("Rent", "Rent"),
    ("Lease", "Lease"),
)

UNITS = (
    (" ", "No Units"),
    ("K", "K"),
    ("M", "M"),

)


class Property(models.Model):
    name = models.CharField(max_length=30)
    slug = AutoSlugField(populate_from='name', unique=True)
    seller = models.CharField(default="Seller", max_length=100)
    date_posted = models.DateField(auto_now_add=True)
    rooms = models.DecimalField(
        decimal_places=0, max_digits=5)
    bedrooms = models.DecimalField(
        decimal_places=0, max_digits=5, blank=True, null=True)
    bathrooms = models.DecimalField(
        decimal_places=0, max_digits=5, blank=True, null=True)
    sqfts = models.DecimalField(
        decimal_places=0, max_digits=5, blank=True, null=True)
    size = models.CharField(default="For Land only", max_length=100, null=True)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="properties")
    type_for = models.CharField(choices=CATEGORIES, max_length=10)
    region = models.ForeignKey(
        Region, on_delete=models.CASCADE, related_name="properties")
    price = models.IntegerField()
    price_units = models.CharField(max_length=10, choices=UNITS)
    short_description = models.CharField(max_length=60)
    description = models.TextField()
    featured = models.BooleanField(default=False)
    image_1 = models.ImageField(upload_to="images")
    image_2 = models.ImageField(upload_to="images")
    image_3 = models.ImageField(upload_to="images")
    image_4 = models.ImageField(upload_to="images")
    image_5 = models.ImageField(upload_to="images")
    image_6 = models.ImageField(upload_to="images")

    class Meta:
        ordering = ('-date_posted', '-id')

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=50)
    message = models.TextField(max_length=255)
    date_posted = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ('-date_posted', '-id')

    def __str__(self):
        return self.name


class Booking(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=15)
    location = models.CharField(max_length=50)
    date_posted = models.DateField(auto_now_add=True)
    propert = models.ForeignKey(
        Property, on_delete=models.CASCADE, related_name="properties")

    class Meta:
        ordering = ('-date_posted', '-id')

    def __str__(self):
        return self.name

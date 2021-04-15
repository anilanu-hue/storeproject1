from datetime import datetime

from django.contrib.auth.models import User
from django.db import models


# Create your models here.
from django.utils.safestring import mark_safe


class BaseClass(models.Model):
    LastmodifiedOn = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(default=datetime.now())
    IsActive = models.BooleanField(max_length=30)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    class Meta:
        abstract = True


class Category(BaseClass):
    MCName = models.CharField(max_length=30, unique=True)
    image = models.ImageField(upload_to="cat_pics", blank=True)

    def __str__(self):
        return self.MCName

    def allCats(self):
        cats = Category.objects.all()
        return cats

    def cat_image1(self):
        if self.image:
            return mark_safe('<img src="/media/%s" width="50" height="50">' % (self.image))
        else:
            return mark_safe('<img  src="/static/images/blank.png" width="50" height="50">')

    cat_image1.short_description = 'CategoryImage'


class SubCategory(BaseClass):
    MC = models.ForeignKey(Category, on_delete=models.CASCADE)
    SCName = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.SCName



class DetailCategory(BaseClass):
    SC = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    DCName = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.DCName

class Brand(BaseClass):
    DC = models.ForeignKey(DetailCategory, on_delete=models.CASCADE, blank=False)
    SC = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    BName = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.BName


from django.db import models


class City(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'freshmart_city'


class Products(BaseClass):
    types = (
        ('daily', 'Daily'),
        ('weekly', 'Weekly'),
        ('monthly', 'Monthly'),
    )
    MC = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    SC = models.ForeignKey(SubCategory, on_delete=models.CASCADE, blank=True, null=True)
    DC = models.ForeignKey(DetailCategory, on_delete=models.CASCADE, blank=True, null=True)
    Brand = models.ForeignKey(Brand, on_delete=models.CASCADE, blank=True, null=True)
    pname = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, null=True, blank=True)
    quantity = models.IntegerField()
    unit_quantity = models.IntegerField(default=0)
    batch_no = models.CharField(max_length=30, blank=True, null=True)
    expiry_date = models.DateField(blank=True, null=True)
    prod_desc = models.TextField(null=True, blank=True)
    mrp = models.FloatField()
    total_price = models.FloatField()
    landing_price = models.FloatField()
    selling_price = models.FloatField()
    offer_perc = models.IntegerField(blank=True, default=0)
    offer_type = models.CharField(max_length=30, choices=types, blank=True, null=True)
    offer_from = models.DateField(blank=True, null=True)
    offer_to = models.DateField(blank=True, null=True)
    image1 = models.ImageField(upload_to="pics1", blank=True)
    image2 = models.ImageField(upload_to="pics2", blank=True)
    image3 = models.ImageField(upload_to="pics3", blank=True)
    image4 = models.ImageField(upload_to="pics4", blank=True)
    offer_price = models.FloatField()
    is_offer = models.BooleanField(default=False)


    def __str__(self):
      return self.pname

    class meta:
        db_table='freshmart_products'


    def image_tag1(self):
        if self.image1:
            return mark_safe('<img src="/media/%s" width="50" height="50">' % (self.image1))
        else:
            return mark_safe('<img  src="/static/images/blank.png" width="50" height="50">')


    image_tag1.short_description = 'Image1'


    def image_tag2(self):
        if self.image2:
            return mark_safe('<img src="/media/%s" width="50" height="50">' % (self.image2))
        else:
            return mark_safe('<img  src="/static/images/blank.png" width="50" height="50">')


    image_tag2.short_description = 'Image2'


    def image_tag3(self):
        if self.image3:
            return mark_safe('<img src="/media/%s" width="50" height="50">' % (self.image3))
        else:
            return mark_safe('<img  src="/static/images/blank.png" width="50" height="50">')


    image_tag3.short_description = 'Image3'


    def image_tag4(self):
        if self.image4:
            return mark_safe('<img src="/media/%s" width="50" height="50">' % (self.image4))
        else:
            return mark_safe('<img src="/static/images/blank.png" width="50" height="50">')


    image_tag4.short_description = 'Image4'


    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'MC':
            kwargs["queryset"] = SubCategory.objects.filter(MC=self.MC)
            return db_field.formfield(**kwargs)
        if db_field.name == 'Brand':
            kwargs["queryset"] = Brand.objects.get(id=self.Brand)
            return db_field.formfield(**kwargs)

        if db_field.name == 'SC':
            kwargs["queryset"] = SubCategory.objects.get(id=self.SC)
            return db_field.formfield(**kwargs)


    # return super(SubCategoryAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_total_price(self):
        total_price = 0
        if self.quantity and self.mrp:
            total_price = self.quantity * self.mrp
        return total_price


    get_total_price.short_description = 'TotalPrice'


    def get_discount(self):
        if self.offer_perc:
            discount = (self.offer_perc / float('100')) * self.selling_price
            return discount
        return float('0')



    def get_offer_price_after_discount(self):
        return self.selling_price - self.get_discount()

    def save(self, *args, **kwargs):
        self.offer_price = str(self.get_offer_price_after_discount())
        super(Products, self).save(*args, **kwargs)


    @staticmethod
    def get_products_by_id(ids):
        return Products.objects.filter(id__in=ids)


    @staticmethod
    def get_all_products():
        return Products.objects.all()


    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return Products.objects.filter(category=category_id)
        else:
            return Products.get_all_products();


class registrationmodel(models.Model):
        name=models.CharField(max_length=15)
        email=models.EmailField(max_length=30)
        password=models.CharField(max_length=20)

class authenticate1(models.Model):

        email=models.EmailField(max_length=30,null=True)
        password = models.CharField(max_length=20,null=True)


class signup(models.Model):
        username = models.CharField(max_length=20)
        password = models.CharField(max_length=25)
        email = models.EmailField(max_length=50)
        first_name = models.CharField(max_length=25)
        last_name = models.CharField(max_length=25)

        def __str__(self):
          return self.name


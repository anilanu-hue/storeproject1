from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm

from django.contrib.auth.models import User

# Create your views here.
import smtplib

from email.mime.multipart import MIMEMultipart

from rest_framework import viewsets
from django.conf import settings
from django.db.models import Sum

from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.

from django.template.backends import django
from spencersapp.models import Products

from spencersapp.models import Category

from spencersapp.models import City

from spencersapp.models import SubCategory, DetailCategory

# from spencersapp.models import registrationmodel

from .forms import singnupform, UserUpdateForm
from spencerscart.models import Orders

from spencerscart.models import CartOrders
# from spencerscart.models import product,price
from api.serializer import catogeryserializer


def index_view(request):
    products = Products.objects.all()
    catgery = Category.objects.all()
    return render(request, 'index.html', {'products': products, 'catgery': catgery})


def about_view(request):
    catgery = Category.objects.all()
    return render(request, 'about.html', {'catgery': catgery})


def shop_view(request):
    catgery = Category.objects.all()
    prod = Products.objects.all()
    return render(request, 'shop.html', {'catgery': catgery, 'prod': prod})


def checkout_view(request):
    catgery = Category.objects.all()
    return render(request, 'checkout.html', {'catgery': catgery})


@login_required
def contactus_view(request):
    catgery = Category.objects.all()
    return render(request, 'contact-us.html', {'catgery': catgery})


def gallery_view(request):
    catgery = Category.objects.all()
    return render(request, 'gallery.html', {'catgery': catgery})


def shopdetail_view(request):
    catgery = Category.objects.all()
    return render(request, 'shop-detail.html', {'catgery': catgery})


def cart_view(request):
    catgery = Category.objects.all()
    return render(request, 'cart.html', {'catgery': catgery})


def myaccount_view(request):
    catgery = Category.objects.all()
    return render(request, 'my-account.html', {'catgery': catgery})


def wishlist_view(request):
    catgery = Category.objects.all()

    return render(request, 'wishlist.html', {'catgery': catgery})


def category(request):
    return render(request, 'catogery.html')


def include_search_view(request):
    catgery = Category.objects.all()
    return render(request, 'include_search_view.html', {'catgery': catgery})


def catsearch_view(request, id):
    products = Products.objects.filter(MC=id)
    return render(request, 'catogery.html', {'products': products})


def directcat_view(request, id):
    y = Products.objects.get(id=id)
    return render(request, 'directcat.html', {'y': y})


@login_required
def myaccount_details(request):
    account_details = User.objects.get(username=request.user)
    return render(request, 'myaccount_details.html', {'account_details': account_details})


def home_view(request):
    return render(request, 'index.html')


def product_search(request):
    if request.method == "POST":
        print(request.POST['pname'])
        pname = request.POST['pname']
        prodsearch = Products.objects.filter(pname__icontains=pname)
        return render(request, 'search_details.html', {'prodsearch': prodsearch})
    return render(request, 'index.html')


def showlist(request):
    if 'term' in request.GET:
        print("hey")
        qs = Products.objects.filter(pname__icontains=request.GET.get('term'))
        print(qs)

        names = list()

        for prod in qs:
            names.append(prod.pname)
            print(prod.pname)
        return JsonResponse(names, safe=False)

    return HttpResponse("hello")


def emailresponse(request):
    if request.method == "POST":
        print(request.POST['Email'])
        receiver_address = request.POST.get('Email')
        sender_address = 'anilkumar1.marolix@gmail.com'
        sender_pass = 'Anil@12345'
        message = MIMEMultipart()
        message['From'] = sender_address
        message['To'] = receiver_address
        message['Subject'] = "Thanks for Subscribing Us !We will come back with great products!! ."

        # attach_file_name = 'email.txt'
        # attach_file = open(attach_file_name, 'r')  # Open the file as binary mode
        # payload = MIMEBase('application', 'octate-stream')
        # payload.set_payload((attach_file).read())
        # encoders.encode_base64(payload)  # encode the attachment
        # add payload header with filename
        # payload.add_header('Content-Decomposition', 'attachment', filename=attach_file_name)
        # message.attach(payload)
        # Create SMTP session for sending the mail
        session = smtplib.SMTP('smtp.gmail.com', 587)  # use gmail with port
        session.starttls()  # enable security
        session.login(sender_address, sender_pass)  # login with mail_id and password
        text = message.as_string()
        session.sendmail(sender_address, receiver_address, text)
        session.quit()
        print('Mail Sent')

        # return render(request, 'contact-us.html')
        return redirect('index_view')
    return HttpResponse("mail sent succesfully")


def signup_view(request):
    catgery = Category.objects.all()
    form1 = singnupform()
    if request.method == "POST":
        form1 = singnupform(request.POST)
        if form1.is_valid():
            result = form1.save()
            result.set_password(result.password)
            result.save()
            return HttpResponseRedirect('/')
    return render(request, 'register.html', {'form1': form1, 'catgery': catgery})


def logout_view(request):
    return render(request, 'logout.html')


def sort_view(request, key):
    if key == "low_to_high":
        prod = Products.objects.all().order_by('selling_price')
    elif key == "high_to_low":
        prod = Products.objects.all().order_by('-selling_price')
    elif key == "newness":
        prod = Products.objects.all().order_by('-created_at')
    else:
        prod = Products.objects.all()
    return render(request, 'sort.html', {'prod': prod})


@login_required
def profile(request):
    if request.method == 'POST':

        u_form = UserUpdateForm(request.POST, instance=request.user)
        if u_form.is_valid():
            u_form.save()

            # messages.success(request,'Your Profile has been updated!')
            return redirect('myaccount_details')
    else:

        u_form = UserUpdateForm(instance=request.user)

    context = {'u_form': u_form}
    return render(request, 'update.html', context)


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('myaccount_details')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'password_change.html', {
        'form': form
    })


'''
def registration_view(request):
    catgery = Category.objects.all()
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        reg = registrationmodel(name=name, email=email, password=password)
        reg.save()

        return redirect('index_view')
    return render(request, 'register.html', {'catgery': catgery})


def user_login(request):
    #context = RequestContext(request)
    if request.method == 'POST':
        Username = request.POST.get('Username')
        Password = request.POST.get('Password')
        user = authenticate(Username=Username, Password=Password)
       # if user is not None:
        if user.is_exist:
                # login(request, user)
                # Redirect to index page.
                return HttpResponse("CORRECT")
        else:
                # Return a 'disabled account' error message
                return HttpResponse("You're account is disabled.")
       # else:
            # Return an 'invalid login' error message.
           # print("invalid login details")
           # return HttpResponse("CORRECT")
            #return render(request,'login.html')
    #else:
        # the login is a  GET request, so just show the user the login form.
       # return render(request,'login.html')




def user_login(request):

    if request.method == 'POST':
        Username = request.POST['Username']
        Password = request.POST['Password']
        user = authenticate(Username=Username, Password=Password)
        if  user is not None:
            return HttpResponse("PLEASE FILL DETAILS CORRECTLY!!")


        else:
            return HttpResponse(' ENTER CORRECT USERNAME AND PASSWORD')


def login_view(request):
    catgery = Category.objects.all()
     return render(request, 'login.html', {'catgery': catgery})
'''


def add_to_cart(request):
    print("hello")
    pid = request.POST['id']
    quan = request.POST['quantity']
    print(quan)
    product = Products.objects.get(id=pid)
    print(product.id)
    if product.is_offer == True:
        price = product.offer_price
    else:
        price = product.selling_price
    try:
        print(request.user)
        user = User.objects.get(username=request.user)
        print(user.id)
        print('try2')
        order = Orders.objects.get(user_id=user.id, is_order=0)
        print("try3")
        try:
            print("try4")
            pre_item = CartOrders.objects.get(product_id=product.id, order_id_id=order.id)
            print("quantity", pre_item.quantity)
            pre_item.quantity = int(pre_item.quantity) + int(quan)
            pre_item.save()
            cart_count = CartOrders.objects.filter(order_id_id=order.id).aggregate(Sum('quantity'))
            request.session['cart_count'] = cart_count['quantity__sum']
            print(request.session['cart_count'])
            # return render(request, 'cartapp/cart_count.html', {'cart_count': request.session['cart_count']})
        except:
            seller_id = product.added_by_id
            cart_item = CartOrders(order_id_id=order.id, user_id=user.id, added_by=seller_id, product_id=product.id,
                                   price=price,
                                   quantity=quan)
            cart_item.save()
            cart_count = CartOrders.objects.filter(order_id_id=order.id).aggregate(Sum('quantity'))
            request.session['cart_count'] = cart_count['quantity__sum']
            # return render(request, 'cartapp/cart_count.html', {'cart_count': request.session['cart_count']})

    except:

        print('aaaaaa')
        order = Orders(user_id=user.id, is_order=0)
        order.save()

        seller_id = product.added_by_id
        cart_item = CartOrders(order_id_id=order.id, product_id=product.id, user_id=user.id, added_by=seller_id,
                               price=price,
                               quantity=quan)
        cart_item.save()
        '''Get Cart Count'''
        cart_count = CartOrders.objects.filter(order_id_id=order.id).aggregate(Sum('quantity'))
        request.session['cart_count'] = cart_count['quantity__sum']
        # return render(request, 'cartapp/cart_count.html', {'cart_count': request.session['car

    return HttpResponse(request.session['cart_count'])

def update_cart(request):

        pid = request.POST['pid']
        oid = request.POST['oid']
        quan = request.POST['quantity']
        obj = CartOrders.objects.get(product_id=pid, order_id_id=oid)
        print("quantity", obj.quantity)
        print(quan)
        obj.quantity = int(obj.quantity) + int(quan)
        print(obj.quantity)
        obj.save()
        cart_count = CartOrders.objects.filter(order_id_id=oid).aggregate(Sum('quantity'))
        request.session['cart_count'] = cart_count['quantity__sum']
        return HttpResponse(request.session['cart_count'])


"""  pid = request.POST['id']
    quan = request.POST['quantity']
    product = Products.objects.get(id=pid)
    price = product.selling_price
    cart_products = CartOrders.objects.select_related('product')
    count = cart_products.count()
    return render(request, 'cart_list.html', {'cart_products': cart_products, 'count': count})"""

def cart_bag(request):
    user = User.objects.get(username=request.user)
    orders = Orders.objects.get(user_id=user.id, is_order=0)

    cart_products = CartOrders.objects.select_related('product').filter(order_id=orders.id)
    count = cart_products.count()

    return render(request, 'cart_list.html', {'cart_products': cart_products, 'count': count})


def cart_del(request, id):
    user = User.objects.get(username=request.user)
    order = Orders.objects.get(user_id=user.id, is_order=0)
    sk = CartOrders.objects.get(id=id).delete()
    cart_count = CartOrders.objects.filter(order_id_id=order.id).aggregate(Sum('quantity'))
    request.session['cart_count'] = cart_count['quantity__sum']
    return redirect('/cart_bag/')





class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('LastmodifiedOn')
    serializer_class = catogeryserializer

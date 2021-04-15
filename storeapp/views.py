import smtplib
from email import encoders
from email.mime.multipart import MIMEMultipart

from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
# Create your views here.
from freshmart.models import Products

from freshmart.models import Category

#from spencersapp.models import registrationmodel

from freshmart.forms import singnupform


def index_view(request):
    products = Products.objects.all()
    catgery = Category.objects.all()
    return render(request, 'index.html', {'products': products, 'catgery': catgery})


def about_view(request):
    catgery = Category.objects.all()
    return render(request, 'about.html', {'catgery': catgery})


def shop_view(request):
    catgery = Category.objects.all()
    return render(request, 'shop.html', {'catgery': catgery})


def checkout_view(request):
    catgery = Category.objects.all()
    return render(request, 'checkout.html', {'catgery': catgery})


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







def home_view(request):
    return render(request, 'index.html')


def product_search(request):
    if request.method == "POST":
        print(request.POST['pname'])
        pname = request.POST['pname']
        q = Products.objects.filter(pname__icontains=pname)
        return render(request, 'search_details.html', {'q': q})
    return render(request, 'index.html')


'''
    product = request.GET['key']
    request.session['product'] = product
    if product != "0":
        search_products = Products.objects.filter(pname__icontains=product)

    else:
         search_products = Products.objects.all()
    context_dict = {'search_products': search_products}
    return render(request,'search_details.html',context_dict)



'''


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

# print(request.POST['word'])
# qs = Products.objects.filter(pname__icontains=request.POST['word'])
'''
from django. contrib. auth import authenticate
    user = authenticate(username='john', password='secret')
        if user is not None: if user. is_active: print "You provided a correct username and password!"
        else: print "Your account has been disabled!"
        else: print "Your username and password were incorrect."
'''





def signup_view(request):
       catgery = Category.objects.all()
       form1 = singnupform()
       if request.method == "POST":
         form1 = singnupform(request.POST)
         if form1.is_valid():
                  result = form1.save()
                  result.set_password(result.password)
                  result.save()
                  return HttpResponseRedirect('/accounts/login')
       return render(request, 'register.html', {'form1': form1, 'catgery': catgery})

def logout_view(request):
    return render(request, 'logout.html')
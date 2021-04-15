from django.shortcuts import render

# Create your views here.
from django.shortcuts import render


# Create your views here.
def home_view(request):
    return render(request, 'home.html')


def homecopy_view(request):
    return render(request, 'homecopy.html')


def mywishlist_view(request):
    return render(request, 'my-wishlist.html')


def product_view(request):
    return render(request, 'product-comparison.html')


def shopping_view(request):
    return render(request, 'shopping-cart.html')


def signin_view(request):
    return render(request, 'sign-in.html')


def terms_view(request):
    return render(request, 'terms-conditions.html')


def blog_view(request):
    return render(request, 'blog.html')


def blogdetail_view(request):
    return render(request, 'blog-details.html')


def category_view(request):
    return render(request, 'category.html')


def checkout_view(request):
    return render(request, 'checkout.html')



def track_view(request):
    return render(request, 'track-orders.html')


def faq_view(request):
    return render(request, 'faq.html')

def hoh_view(request):
    return render(request, '404.html')


def detail_view(request):
    return render(request, 'detail.html')


def contact_view(request):
    return render(request, 'contact.html')


def contactus_view(request):
    return render(request, 'contact-us.html')
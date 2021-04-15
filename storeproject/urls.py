"""storeproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.db import router
from django.urls import path, include
from rest_framework import routers

from spencersapp import views


router = routers.DefaultRouter()
router.register(r'users', views.CategoryView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index_view, name='index_view'),
    path('about_view/', views.about_view, name='about_view'),
    path('shop_view/', views.shop_view, name='shop_view'),
    path('checkout_view/', views.checkout_view, name='checkout_view'),
    path('contactus_view/', views.contactus_view, name='contactus_view'),
    path('gallery_view/', views.gallery_view, name='gallery_view'),
    path('shopdetail_view/', views.shopdetail_view, name='shopdetail_view'),
    path('cart_view/', views.cart_view, name='cart_view'),
    path('myaccount_view/', views.myaccount_view, name='myaccount_view'),
    path('wishlist_view/', views.wishlist_view, name='wishlist_view'),
    path('category/', views.category, name='category'),
    path('include_search_view/', views.include_search_view, name='include_search_view'),
    path('catsearch_view/<int:id>', views.catsearch_view, name='catsearch_view'),
    #   path('registration_view/', views.registration_view, name='registration_view'),
    # path('login_view/', views.login_view, name='login_view'),
    path('home_view/', views.home_view, name='home_view'),
    path('directcat_view/<int:id>', views.directcat_view, name='directcat_view'),
    path('showlist/', views.showlist, name='showlist'),
    path('product_search/', views.product_search, name='product_search'),
    path('emailresponse/', views.emailresponse, name='emailresponse'),
    #    path('user_login/', views.user_login, name='user_login'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', views.signup_view, name='signup'),
    path('accounts/logout/', views.logout_view, name='logout_view'),
    path('myaccount_details/', views.myaccount_details, name='myaccount_details'),
    path('sort/<str:key>', views.sort_view, name='sort'),
    path('profile/', views.profile, name='profile'),
    path('change_password/', views.change_password, name='change_password'),
    path('addcart/',views.add_to_cart, name='addcart'),
    path('cart_bag/', views.cart_bag, name='cart_bag'),
    path('update_cart/', views.update_cart, name='update_cart'),
    path('cart_del/<int:id>', views.cart_del, name='cart_del'),
    path('', include(router.urls)),
    path('users/', include('rest_framework.urls', namespace='rest_framework'))
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




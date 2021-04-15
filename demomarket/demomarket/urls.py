"""demomarket URL Configuration

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
from django.contrib import admin
from django.urls import path

from demomarket import settings

"""MarolixMart URL Configuration

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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path


from demoapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view, name='homeview'),
    path('homecopy_view/', views.homecopy_view, name='homecopy_view'),
    path('mywishlist_view/', views.mywishlist_view, name='mywishlist_view'),
    path('product_view/', views.product_view, name='product_view'),
    path('shopping_view/', views.shopping_view, name='shopping_view'),
    path('signin_view/', views.signin_view, name='signin_view'),
    path('terms_view/', views.terms_view, name='terms_view'),
    path('blog_view/', views.blog_view, name='blog_view'),
    path('blogdetail_view/', views.blogdetail_view, name='blogdetail_view'),
    path('category_view/', views.category_view, name='category_view'),
    path('checkout_view/', views.checkout_view, name='checkout_view'),
    path('track_view/', views.track_view, name='track_view'),
    path('faq_view/', views.faq_view, name='faq_view'),
    path('hoh_view/', views.hoh_view, name='hoh_view'),
    path('detail_view/', views.detail_view, name='detail_view'),
    path('contact_view/', views.contact_view, name='contact_view'),
    path('contactus_view/', views.contactus_view, name='contactus_view'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



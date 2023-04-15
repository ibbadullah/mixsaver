"""mixsaver URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .sitemaps import BrandsSitemap, ProductsSitemap, StaticSitemap, ArticlesSitemap
from django.contrib.sitemaps.views import sitemap

# Site map setting
sitemaps = {
    'staticsitemap': StaticSitemap,
    'articlesSitemap': ArticlesSitemap,
    'brands': BrandsSitemap,
    'products': ProductsSitemap,
}


urlpatterns = [
    path('sitemap.xml',sitemap,{'sitemaps':sitemaps}),
    path('robots.txt',include('robots.urls')),
    path('192-168-2-1/', admin.site.urls),
    path('',include('publicsection.urls')),
    path('',include('usersaccountsection.url')),

]



# Setting up media folder
urlpatterns= urlpatterns + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

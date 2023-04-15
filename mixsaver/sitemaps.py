from django.contrib.sitemaps import Sitemap
from administrationsection.models import BrandsModel, CouponProducts
from publicsection.models import ArticlesModel
from django.shortcuts import reverse

# Sitemap class for static pages
class StaticSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return ['Home','TodayTopDeals','HotDeals','AllCouponWebsites','LoginView','SignUpView','resest_password','Sitemap','ContactUsView']

    def location(self, item):
        return reverse(item)


# Sitemap class for articles
class ArticlesSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return ArticlesModel.objects.all()


# Sitemap class for brands
class BrandsSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return BrandsModel.objects.all()


# Sitemap class for sitemap products
class ProductsSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return CouponProducts.objects.filter(CouponStatus='Active')






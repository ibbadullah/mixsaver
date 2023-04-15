from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name="Home"),
    path('contact-us/',ContactUsView.as_view(),name="ContactUsView"),
    path('newsletter/',NewsletterView.as_view(),name="NewsletterView"),
    path('coupon-code-websites/',displyAllCouponWebsitese,name="AllCouponWebsites"),
    path('today-top-deals/',TodayTopDealsView.as_view(),name="TodayTopDeals"),
    path('search-today-top-deals/',todayTopDealsSearchView.as_view(),name="TodayTopDealsSearch"),
    path('hot-deals/',TodayHotDealsView,name="HotDeals"),
    path('<str:slug>/coupon-codes/',BrandAllProductsViews,name="BrandAllProducts"),
    path('deals/<str:slug>/',DynamicBrandsProductsSearchView.as_view(),name="DynamicBrandsProductsSearch"),
    path('coupon-code/<str:slug>/',couponDetailsView,name="CouponDetailsViewStatic"),
    path('mobile-app/',MobileAppsComingSoonView,name="MobileApp"),
    path('article/<str:slug>/',ArticlesView.as_view(),name="Articles"),
    path('sitemap/',sitemapView,name="Sitemap"),
    path('blog/',blogView,name="BlogView"),
]

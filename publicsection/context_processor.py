from administrationsection.models import NotificationModel,CouponProducts, BrandsModel, Categories
from usersaccountsection.models import Accounts


# All brands context processor
def allBrands(request):
    query = BrandsModel.objects.all()
    return {"AllBrands":query}


# All categories context processor
def allCategories(request):
    query = Categories.objects.all()
    return {"Categories":query}


# All users
def allUsers(request):
    query = Accounts.objects.all().count()
    return {"AllUsers":query}


# Context processor for displaying trending deals
def tenTrendingDeal(request):
    query = CouponProducts.objects.filter(CouponStatus="Active").order_by('-CouponProductDisplayPrice').order_by('?')[0:10]
    return {"TenTrendingDeals":query}


# Context processor for displaying trending deals
def tenBestDeals(request):
    query = CouponProducts.objects.filter(CouponStatus="Active",CouponProductRating__gte=4.5).order_by('?')[0:10]
    return {"TenBestDeals":query}


# Context processor for total brands
def totalBrands(request):
    query = BrandsModel.objects.all().count()
    return {"TotalBrands":query}


# Context processor for total brands
def totalCoupons(request):
    query = CouponProducts.objects.all().count()
    return {"TotalCoupons":query}


# Context processor for total brands
def totalActiveCoupons(request):
    query = CouponProducts.objects.filter(CouponStatus="Active").count()
    return {"TotalActiveCoupons":query}


# Context processor for notifications
def firstThreeNotifications(request):
    notifications = NotificationModel.objects.filter(Status='Active').order_by('-id')[0:3]
    return {"getFirstThreeNotifications":notifications}


def allNotifications(request):
    notifications = NotificationModel.objects.filter(Status='Active').order_by('-id')
    return {"getAllNotifactions":notifications}

from django.shortcuts import render, HttpResponse
from django.views import View
from administrationsection.models import ContactUsModel, NewsletterModel, BrandsModel, CouponProducts
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from .other_logics import saveUserQuery, keywordsSeparator
from .models import ArticlesModel
from usersaccountsection.sezona import sez1, sez2


# Home function
def home(request):
    try:
        # Taking 10 best items from below three brands for home page
        amazonDeals = CouponProducts.objects.filter(Brand__BrandName='Amazon').order_by('-CouponProductRating').order_by('?')[0:10]
        aliexpressDeals = CouponProducts.objects.filter(Brand__BrandName='Aliexpress').order_by('-CouponProductRating').order_by('?')[0:10]
        
        return render(request, 'public-section/index.html',{"AmazonDeals":amazonDeals,"AliexpressDeals":aliexpressDeals})
    except:
        return render(request,'public-section/404.html')


# Page current url returning
def pageCurrentUrl(request):
    getPageUrl = request._current_scheme_host+request.path
    return getPageUrl


# Newsletter view
class NewsletterView(View):
    def post(self,request):
        if request.POST:
            email = sez1(request,request.POST['email'])
            query = NewsletterModel(Email=email)
            if NewsletterModel.objects.filter(Email=email).exists():
                title = "Newsletters are already activated!"
                message = "Dear user newsletters are already activated for "+sez2(request,email)+". Thanks for your interest."
                return render(request, 'public-section/newsletter-message.html', {"title": title, "messaage": message})
            else:
                query.save()
                title = "Newsletter Subscribed Successfully!"
                message = "Dear user newsletter has been subscribed successfully to your email. Now you will get notified about exclusive deals of all big brands. Thank you for subscribing newsletter."
                return render(request,'public-section/newsletter-message.html',{"title": title,"messaage": message})

    def get(self,request):
        return HttpResponse("<h2>Invalid request.</h2>")

# Class base view of contact us
class ContactUsView(View):
    def get(self,request):
        pageUrl = pageCurrentUrl(request)
        return render(request,'public-section/contact-us.html',{"pageUrl":pageUrl})

    def post(self,request):
        if request.POST:
            fullName = sez1(request,request.POST['full-name'])
            title = sez1(request,request.POST['title'])
            department = sez1(request,request.POST['department'])
            email = sez1(request,request.POST['email'])
            message = sez1(request,request.POST['message'])
            query = ContactUsModel(FullName=fullName,MessageTitle=title,Department=department,EmailAddress=email,Message=message)
            query.save()
            if query:
                messages.info(request,"Dear "+sez2(request,fullName)+" your message sent successfully.")
                return render(request,'public-section/contact-us.html')
            else:
                messages.info(request,"Something went wrong!")
                return render(request,'public-section/contact-us.html')


# view for displaying all coupons websites
def displyAllCouponWebsitese(request):
    if request.method == "GET":
        query = BrandsModel.objects.all()
        paginator = Paginator(query,12) # From paginator class passing the query and limit
        page = request.GET.get('page') # Defining url variable
        query = paginator.get_page(page) # Getting the current page products
        return render(request,'public-section/all-brands-coupon-codes-websites.html',{"Data":query})
    else:
        return HttpResponse("<h2>Invalid request.</h2>")


# class base view for today top deals
class TodayTopDealsView(View):
    def get(self,request):
        if request.method == "GET":
            query = CouponProducts.objects.filter(CouponStatus="Active",CouponProductRating__gte=4.5)
            # Pagination
            paginator = Paginator(query,15)  # From paginator class passing the query and limit
            page = request.GET.get('page')  # Defining url variable
            query = paginator.get_page(page)  # Getting the current page products
            # Calling current page url function
            pageUrl = pageCurrentUrl(request)
            return render(request,'public-section/today-top-deals.html',{"Data":query,"pageUrl":pageUrl})


# View for today top deals searching
class todayTopDealsSearchView(View):
    def get(self,request):
        try:
            if request.method == "GET":
                category = request.GET.get('category')
                userQuery = request.GET.get('q')
                pricefilter = request.GET.get('price-low-high')
                activefilter =request.GET.get('active-deals')
                # Saving user query calling user query saving function
                saveUserQuery(request,userQuery,category)
                # Checking if user selected all categories and also apply any filter
                if category == "all" and pricefilter or activefilter in request.GET:
                    query = CouponProducts.objects.filter(Q(CouponProductTitle__icontains=userQuery)
                                                          | Q(CouponProductKeywords__icontains=userQuery)
                                                          | Q(CouponProductDescription__icontains=userQuery),
                                                          CouponStatus="Active").order_by('CouponProductPrice')
                    querycounter = query.count()
                    paginator = Paginator(query, 10)  # From paginator class passing the query and limit
                    page = request.GET.get('page')  # Defining url variable
                    query = paginator.get_page(page)  # Getting the current page products
                    return render(request, 'public-section/searchItemsHorizontically.html',
                                  {"Data":query,"UserQuery": userQuery,"category":category,"query":userQuery,"pricefilter":pricefilter,"activefilter":activefilter,"Count":querycounter})

                # Checking if user just selected all categories
                elif category == "all":
                    query = CouponProducts.objects.filter(Q(CouponProductTitle__icontains=userQuery)|Q(CouponProductKeywords__icontains=userQuery)|Q(CouponProductDescription__icontains=userQuery),CouponStatus="Active")
                    querycounter = query.count()
                    paginator = Paginator(query, 10)  # From paginator class passing the query and limit
                    page = request.GET.get('page')  # Defining url variable
                    query = paginator.get_page(page)  # Getting the current page products
                    return render(request, 'public-section/searchItemsHorizontically.html',
                                  {"Data": query, "UserQuery": userQuery, "category": category, "query": userQuery,
                                    "pricefilter": pricefilter, "activefilter": activefilter,
                                   "Count": querycounter})

                # Checking if user selected any category and also apply filter
                elif category != "all" and pricefilter or activefilter in request.GET:
                    query = CouponProducts.objects.filter(Q(CouponProductTitle__icontains=userQuery)
                                                          | Q(CouponProductKeywords__icontains=userQuery)
                                                          | Q(CouponProductDescription__icontains=userQuery),
                                                          CouponStatus="Active",Category__CategoryName=category).order_by('CouponProductPrice')
                    querycounter = query.count()
                    paginator = Paginator(query, 10)  # From paginator class passing the query and limit
                    page = request.GET.get('page')  # Defining url variable
                    query = paginator.get_page(page)  # Getting the current page products
                    return render(request, 'public-section/searchItemsHorizontically.html',
                                  {"Data": query, "UserQuery": userQuery, "category": category, "query": userQuery,
                                    "pricefilter": pricefilter, "activefilter": activefilter,
                                   "Count": querycounter})

                else:
                    query = CouponProducts.objects.filter(Q(CouponProductKeywords__icontains=userQuery)
                                                          | Q(CouponProductTitle__icontains=userQuery)
                                                          | Q(CouponProductDescription__icontains=userQuery),
                                                          CouponStatus="Active", Category__CategoryName=category)
                    querycounter = query.count()
                    paginator = Paginator(query, 10)  # From paginator class passing the query and limit
                    page = request.GET.get('page')  # Defining url variable
                    query = paginator.get_page(page)  # Getting the current page products
                    return render(request, 'public-section/searchItemsHorizontically.html',
                                  {"Data": query, "UserQuery": userQuery, "category": category,"query":userQuery,"pricefilter":pricefilter,"activefilter":activefilter,"Count":querycounter})
        except:
            return HttpResponse("<h3>Invalid request.</h3>")


# Today Hot deals
def TodayHotDealsView(request):
    if request.method == "GET":
        query = CouponProducts.objects.filter(CouponStatus="Active",CouponProductRating__gte=4.2).order_by('CouponProductPrice')
        # Pagination
        paginator = Paginator(query,15)  # From paginator class passing the query and limit
        page = request.GET.get('page')  # Defining url variable
        query = paginator.get_page(page)  # Getting the current page products
        # Calling current page url function
        pageUrl = pageCurrentUrl(request)
        return render(request,'public-section/hot-deals.html',{"Data":query,"pageUrl":pageUrl})



# Coupon Details View
def couponDetailsView(request,slug):
    try:
        pageUrl =pageCurrentUrl(request)
        query = CouponProducts.objects.get(CouponProductSlug=slug)
        # Query for displaying related products in the bottom
        productTitle = query.CouponProductTitle
        productKeywords = query.CouponProductKeywords
        headerKeywords = productKeywords
        bottomKeywords = keywordsSeparator(headerKeywords)
        relatedQuery = CouponProducts.objects.filter(Q(CouponProductTitle__icontains=productTitle)|Q(CouponProductKeywords__icontains=productKeywords)).exclude(CouponProductTitle=productTitle)[0:10]
        return render(request,'public-section/productDetailsPage.html',{"Data":query,"pageUrl":pageUrl,"RelatedProducts":relatedQuery,"HeaderKeywords":headerKeywords,"BottomKeywords":bottomKeywords})
    except:
        return render(request,'public-section/404.html')



# Brand all products 
def BrandAllProductsViews(request,slug):
    try:
        if request.method == "GET":
            brandSlug = BrandsModel.objects.get(BrandSlug=slug)
            brandName = brandSlug.BrandName
            brandTitle = brandSlug.BrandTitle
            brandKeywords = brandSlug.BrandKeywords
            brandDescription = brandSlug.BrandDescription
            query = CouponProducts.objects.filter(CouponStatus="Active",Brand__BrandName=brandName).order_by('-id')
            # Counting total products
            Counting = query.count()
            # Separating keywords by comma
            keywords = keywordsSeparator(brandKeywords)
            # Pagination
            paginator = Paginator(query, 15)  # From paginator class passing the query and limit
            page = request.GET.get('page')  # Defining url variable
            query = paginator.get_page(page)  # Getting the current page products
            # Calling current page url function
            pageUrl = pageCurrentUrl(request)
            return render(request, 'public-section/brand-all-products.html', {"Data": query,"BrandName":brandName,"BrandTitle":brandTitle,"BrandSlug":brandSlug.BrandSlug,"Counter":Counting, "pageUrl": pageUrl,"Keyords":keywords,"HeadKeywords":brandKeywords,"BrandDescription":brandDescription,"Brandlogo":brandSlug.BrandLogo})
    except:
        return render(request,'public-section/404.html')


# View for dynamic brand products searching
class DynamicBrandsProductsSearchView(View):
    def get(self,request,slug):
        try:
            if request.method == "GET":
                category = request.GET.get('category')
                userQuery = request.GET.get('q')
                pricefilter = request.GET.get('price-low-high')
                activefilter =request.GET.get('active-deals')
                # Calling getting current url function
                pageUrl = pageCurrentUrl(request)
                # Saving user query calling user query saving function
                saveUserQuery(request,userQuery,category)
                # Getting brand slug
                brandQuery = BrandsModel.objects.get(BrandSlug=slug)
                brandName = brandQuery.BrandName
                # Checking if user selected all categories and also apply any filter
                if category == "all" and pricefilter or activefilter in request.GET:
                    query = CouponProducts.objects.filter(Q(CouponProductTitle__icontains=userQuery)
                                                          | Q(CouponProductKeywords__icontains=userQuery)
                                                          | Q(CouponProductDescription__icontains=userQuery),
                                                          CouponStatus="Active",Brand__BrandName=brandName).order_by('CouponProductPrice')
                    querycounter = query.count()
                    paginator = Paginator(query, 10)  # From paginator class passing the query and limit
                    page = request.GET.get('page')  # Defining url variable
                    query = paginator.get_page(page)  # Getting the current page products
                    return render(request, 'public-section/DynamicSearchItemsHorizontically.html',{"Data":query,"UserQuery": userQuery,"query":userQuery,"category":category,"pricefilter":pricefilter,"activefilter":activefilter,"Count":querycounter,"BrandSlug":brandQuery.BrandSlug,"pageUrl":pageUrl})

                # Checking if user just selected all categories
                elif category == "all":
                    query = CouponProducts.objects.filter(Q(CouponProductTitle__icontains=userQuery)|Q(CouponProductKeywords__icontains=userQuery)|Q(CouponProductDescription__icontains=userQuery),CouponStatus="Active",Brand__BrandName=brandName)
                    querycounter = query.count()
                    paginator = Paginator(query, 10)  # From paginator class passing the query and limit
                    page = request.GET.get('page')  # Defining url variable
                    query = paginator.get_page(page)  # Getting the current page products
                    return render(request, 'public-section/DynamicSearchItemsHorizontically.html',{"Data": query, "UserQuery": userQuery, "category": category, "query": userQuery,"pricefilter": pricefilter, "activefilter": activefilter,"Count": querycounter,"BrandSlug":brandQuery.BrandSlug,"pageUrl":pageUrl})

                # Checking if user selected any category and also apply filter
                elif category != "all" and pricefilter or activefilter in request.GET:
                    query = CouponProducts.objects.filter(Q(CouponProductTitle__icontains=userQuery)
                                                          | Q(CouponProductKeywords__icontains=userQuery)
                                                          | Q(CouponProductDescription__icontains=userQuery),
                                                          CouponStatus="Active",Category__CategoryName=category,Brand__BrandName=brandName).order_by('CouponProductPrice')
                    querycounter = query.count()
                    paginator = Paginator(query, 10)  # From paginator class passing the query and limit
                    page = request.GET.get('page')  # Defining url variable
                    query = paginator.get_page(page)  # Getting the current page products
                    return render(request, 'public-section/DynamicSearchItemsHorizontically.html',{"Data": query, "UserQuery": userQuery, "category": category, "query": userQuery,"pricefilter": pricefilter, "activefilter": activefilter,"Count": querycounter,"BrandSlug":brandQuery.BrandSlug,"pageUrl":pageUrl})

                    # Checking if user selected any category and also apply filter
                elif category is None and userQuery is None:
                    query = CouponProducts.objects.filter(CouponStatus="Active",Brand__BrandName=brandName).order_by('CouponProductPrice')
                    InfoQuery = brandQuery
                    querycounter = query.count()
                    paginator = Paginator(query, 10)  # From paginator class passing the query and limit
                    page = request.GET.get('page')  # Defining url variable
                    query = paginator.get_page(page)  # Getting the current page products
                    return render(request, 'public-section/DynamicSearchItemsHorizontically.html',
                                  {"Data": query, "UserQuery": userQuery, "category": category, "query": userQuery,
                                   "pricefilter": pricefilter, "activefilter": activefilter, "Count": querycounter,
                                   "BrandSlug": brandQuery.BrandSlug, "pageUrl": pageUrl,"InfoQuery":InfoQuery})

                else:
                    query = CouponProducts.objects.filter(Q(CouponProductKeywords__icontains=userQuery)
                                                          | Q(CouponProductTitle__icontains=userQuery)
                                                          | Q(CouponProductDescription__icontains=userQuery),
                                                          CouponStatus="Active", Category__CategoryName=category,Brand__BrandName=brandName).order_by('-CouponProductRating')
                    querycounter = query.count()
                    paginator = Paginator(query, 10)  # From paginator class passing the query and limit
                    page = request.GET.get('page')  # Defining url variable
                    query = paginator.get_page(page)  # Getting the current page products
                    return render(request, 'public-section/DynamicSearchItemsHorizontically.html',{"Data": query, "UserQuery": userQuery, "category": category,"query":userQuery,"pricefilter":pricefilter,"activefilter":activefilter,"Count":querycounter,"BrandSlug":brandQuery.BrandSlug,"pageUrl":pageUrl})
        except ValueError as err:
            return HttpResponse(err)


# Apps coming soon view
def MobileAppsComingSoonView(request):
    if request.method == "GET":
        AppDownloadRequest = request.GET.get('app')
        if AppDownloadRequest == 'Android':
            return render(request,'public-section/mobile-app.html',{"App":"Android"})
        else:
            return render(request, 'public-section/mobile-app.html', {"App": "IOS"})
    else:
        return render(request,'public-section/404.html')


# View for Articles
class ArticlesView(View):
    def get(self,request,slug):
        try:
            # Calling current page url for getting current page url
            pageUrl = pageCurrentUrl(request)
            query = ArticlesModel.objects.get(ArticleSlug=slug)
            return render(request,'articles/article-base.html',{"Data":query,"pageUrl":pageUrl})
        except:
            return render(request,'public-section/404.html')


# view for sitemap.html I mean for users sitemap
def sitemapView(request):
    try:
        if request.method == "GET":
            return render(request,'public-section/sitemap.html')
        else:
            return HttpResponse("<h2>Invalid request.</h2>")
    except:
        return render(request,'public-section/404.html')





# blog view
def blogView(request):
    query = ArticlesModel.objects.all()
    pagination = Paginator(query,10)
    page = request.GET.get('page')
    query = pagination.get_page(page)
    return render(request,'public-section/blog.html',{"Data":query})

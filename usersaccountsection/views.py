from django.shortcuts import render, redirect, HttpResponse
from publicsection.views import pageCurrentUrl
from django.views import View
from .models import Accounts, UserData, LoginHistoryModel
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from publicsection.other_logics import getIp
from administrationsection.models import NotificationModel, CouponProducts
from django.core.paginator import Paginator
from .sezona import sez1, sez2


# Create your views here.
# Login View
class LoginView(View):
    def get(self,request):
        if request.user.is_authenticated:
            return redirect('DashboardView')
        else:
            pageUrl = pageCurrentUrl(request)
            return render(request, 'public-section/login.html', {"pageUrl": pageUrl})

    def post(self,request):
        if request.method == 'POST':
            email = request.POST['email'].lower()
            password = request.POST['password']
            user = authenticate(email=email,password=password)
            if user is not None:
                login(request,user)
                ip = getIp(request)
                LoginHistoryModel.objects.create(user=request.user,IpAddress=ip)
                return redirect('DashboardView')
            else:
                messages.info(request,"You entered invalid credentials.")
                return redirect('LoginView')



# Sign Up View
class SignupView(View):
    def get(self,request):
        if request.user.is_authenticated:
            return redirect('DashboardView')
        else:
            pageUrl = pageCurrentUrl(request)
            return render(request,'public-section/sign-up.html',{"pageUrl":pageUrl})

    def post(self,request):
        if request.POST:
            firstName = sez1(request,request.POST['first-name'])
            lastName = sez1(request,request.POST['last-name'])
            username = sez1(request,request.POST['username'])
            email = request.POST['email'].lower()
            password = request.POST['password']
            # Checking if email already exist in the database
            if Accounts.objects.filter(email=email).exists():
                messages.info(request,'An account is already created on '+email+". Please use another email.")
                return redirect('SignUpView')
            elif Accounts.objects.filter(username=username).exists():
                messages.info(request,"Username already exists. Please choose another one.")
                return redirect('SignUpView')
            else:
                user = Accounts.objects.create_user(first_name=firstName, last_name=lastName, username=username,
                                                    email=email, password=password)
                user.save()
                user = login(request,user)
                return redirect('DashboardView')


# View for loadinq  g dashboard
@login_required(login_url='LoginView')
def DashbordView(request):
    if request.user.is_authenticated:
        return render(request,'user-account-section/index.html')
    else:
        return HttpResponse("<h1>Invalid request.</h1>")

# View for logout
def LogoutView(request):
    logout(request)
    messages.info(request,'You have signed out from your mixsaver.com account.')
    return redirect('LoginView')


# Setting class based view
class SettingView(View):
    def get(self,request):
        if request.user.is_authenticated:
            secondaryEmail = UserData.objects.filter(User=request.user.id)
            return render(request,'user-account-section/settings.html',{"secondaryEmail":secondaryEmail})
        else:
            return redirect('LoginView')
    def post(self,request):
        if request.method == 'POST':
           firstName = sez1(request,request.POST['first-name'])
           lastName = sez1(request,request.POST['last-name'])
           user = Accounts.objects.get(id=request.user.id)
           user.first_name = firstName
           user.last_name = lastName
           user.save()
           if user is not None:
               messages.info(request,'Account updated successfully.')
               return redirect('Settings')
           else:
               messages.info(request, 'Something went wrong.')
               return redirect('Settings')


# View for adding secondary email
@login_required(login_url='LoginView')
def AddSecondaryEmailView(request):
    try:
        if request.method == "POST":
            email = sez1(request, request.POST['email'].lower())
            query = UserData(User_id=request.user.id, UserSecondaryEmail=email)
            query.save()
            if query:
                messages.info(request, "Secondary email added successfully.")
                return redirect('Settings')
            else:
                messages.info(request, "Something went wrong.")
                return redirect('Settings')
    except:
        messages.info(request, "Something went wrong!")
        return redirect('Settings')




# View for updating secondary email
@login_required(login_url='LoginView')
def UpdateSecondaryEmailView(request):
    try:
        if request.method == "POST":
            email = sez1(request, request.POST['email'].lower())
            query = UserData.objects.get(User=request.user.id)
            query.UserSecondaryEmail = email
            query.save()
            if query:
                messages.info(request, "Secondary email updated successfully.")
                return redirect('Settings')
            else:
                messages.info(request, "Something went wrong.")
                return redirect('Settings')
    except:
        messages.info(request, "Something went wrong!")
        return redirect('Settings')


# View for getting login record
@login_required(login_url='LoginView')
def getLoginHistory(request):
    if request.method == "GET":
        getRecord = LoginHistoryModel.objects.filter(user=request.user.id).order_by('-id')
        return render(request,'user-account-section/activity-log.html',{"getRecord":getRecord})
    else:
        return HttpResponse("<h2>Invalid request</h2>")


# View for displaying all notifications
@login_required(login_url='LoginView')
def showAllNotifications(request):
    if request.method == "GET":
        return render(request,'user-account-section/notifications.html')
    else:
        return HttpResponse("<h2>Invalid request.</h2>")


# View for displaying single notification
@login_required(login_url='LoginView')
def getSingleNotification(request,id):
    try:
        if request.method == "GET":
            getSingleNotification = NotificationModel.objects.get(id=id)
            return render(request, 'user-account-section/notification-details.html', {"Details": getSingleNotification})
        else:
            return HttpResponse("<h2>Invalid response.</h2>")
    except:
        return render(request,'public-section/404.html')


# View for displaying my deals
@login_required(login_url='LoginView')
def myDeals(request):
    query = CouponProducts.objects.filter(CouponStatus="Active",CouponProductRating__gte=4.3)
    paginator = Paginator(query, 12)  # From paginator class passing the query and limit
    page = request.GET.get('page')  # Defining url variable
    query = paginator.get_page(page)  # Getting the current page products
    return render(request,'user-account-section/my-deals.html',{"Data":query})









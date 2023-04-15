from .models import UsersSearchQueriesModel
from django.shortcuts import render,redirect, HttpResponse
from usersaccountsection.sezona import sez1

# Function for getting IP address
def getIp(request):
    x_forward = request.META.get("HTTP_X_FORWARDED_FOR")
    if x_forward:
        ip=x_forward.split(',')[0]
    else:
        ip=request.META.get("REMOTE_ADDR")
    return ip


# Function for users search inserting
def saveUserQuery(request,Userquery,Category):
    userIp = getIp(request)

    if Userquery == None and Category == None or Userquery == None or Category == None:
        return ''
    else:
        userIp = sez1(request, userIp)
        Userquery = sez1(request, Userquery)
        Category = sez1(request, Category)
        # first checking the record in the database to avoid from the duplicate records
        ipQuery = UsersSearchQueriesModel.objects.filter(userIp=userIp).exists()
        userQuery = UsersSearchQueriesModel.objects.filter(userQuery=Userquery).exists()
        category = UsersSearchQueriesModel.objects.filter(category=Category).exists()

        if ipQuery and userQuery and category:
            return ''
        elif request.user.is_authenticated:
            userEmail = sez1(request, request.user.email)
            query = UsersSearchQueriesModel(userQuery=Userquery, category=Category, userEmail=userEmail, userIp=userIp)
            return query.save()
        else:
            query = UsersSearchQueriesModel(userQuery=Userquery, category=Category, userIp=userIp)
            return query.save()




# Keywords separation
def keywordsSeparator(keywords):
    words = keywords.split(',')
    return words


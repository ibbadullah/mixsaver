from django.db import models
from django.contrib.auth.models import (AbstractBaseUser,BaseUserManager)


# Rewriting the admin Base user manager. Editing admin.
class MyAccountManager(BaseUserManager):
    # we can pass extra parameters
    def create_user(self,email,username,password,first_name,last_name):
        if not email:
            raise ValueError("User must have an email!")
        if not username:
            raise ValueError("User must have a username!")

        # Now passing the parameter and assigning to default (we can extra pass parameters)
        user = self.model(
            email = self.normalize_email(email),
            username = username,
            first_name = first_name,
            last_name = last_name
        )

        # Saving the admin
        user.set_password(password)
        user.save(using = self._db)
        return user

    def create_superuser(self,email,username,password,first_name,last_name):
        # Now passing parameter and creating super user
        user = self.create_user(
            email = self.normalize_email(email),
            username=username,
            password = password,
            first_name = first_name,
            last_name = last_name,
        )
        # Now changing the booleans values
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        # saving the admin
        user.save(using=self._db)
        return user


# Setting email as login credentail instead if username
class Accounts(AbstractBaseUser):
    email = models.EmailField(verbose_name="email",unique=True)
    username = models.CharField(max_length=25,unique=True)
    date_joined= models.DateTimeField(verbose_name="date joined",auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last login",auto_now=True)
    is_admin= models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff= models.BooleanField(default=False)
    is_superuser= models.BooleanField(default=False)
    first_name=models.CharField(max_length=255,blank=True,null=True,default=False)
    last_name=models.CharField(max_length=255,blank=True,null=True,default=False)
    # Now we're going to set email as login field we can also set phone number

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','first_name','last_name']

    objects = MyAccountManager()

    # Function for returning email
    def __str__(self):
        return self.email
    # Returning the is_admin
    def has_perm(self,perm,obj=None):
        return self.is_admin
    # Giving permission to the admin
    def has_module_perms(self,app_label):
        return True



# User other's data
class UserData(models.Model):
    User = models.ForeignKey(Accounts,related_name="userid",on_delete=models.CASCADE)
    UserSecondaryEmail = models.EmailField(verbose_name="secondaryemail",unique=True)
    class Meta:
        db_table = "userdata"


# Login History model
class LoginHistoryModel(models.Model):
    user = models.ForeignKey(Accounts,on_delete=models.CASCADE)
    Date = models.DateTimeField(auto_now_add=True,null=True)
    IpAddress = models.CharField(max_length=200,null=True,blank=True)
    class Meta:
        db_table = "loginhistory"


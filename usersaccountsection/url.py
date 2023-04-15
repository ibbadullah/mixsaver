from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views
# url goes here

urlpatterns = [
    path('login/', LoginView.as_view(), name="LoginView"),
    path('signup/', SignupView.as_view(), name="SignUpView"),
    path('dashboard/',DashbordView,name="DashboardView"),
    path('logout/',LogoutView,name="LogoutUser"),
    path('dashboard/settings/',SettingView.as_view(),name="Settings"),
    path('update-secondary-email/',UpdateSecondaryEmailView,name="UpdateSecondaryEmail"),
    path('add-secondary-email/',AddSecondaryEmailView, name="AddSecondaryEmail"),
    path('dashboard/activity-log/',getLoginHistory,name="LoginHistory"),
    path('dashboard/notifications/',showAllNotifications,name="ShowAllNotifications"),
    path('dashboard/notification-details/<int:id>/',getSingleNotification,name="GetSingleNotificationDetails"),
    path('dashboard/my-deals/',myDeals,name="MyDeals"),

    # Setting and customizing default views of Password change and forgot
    path('reset_password/',
    auth_views.PasswordResetView.as_view(template_name="password-reset-templates/reset_password.html"),
    name="resest_password"),

    path('reset_password_sent/',
    auth_views.PasswordResetDoneView.as_view(template_name="password-reset-templates/reset_password_sent.html"),
    name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
    auth_views.PasswordResetConfirmView.as_view(template_name="password-reset-templates/reset_password_form.html"),
    name="password_reset_confirm"),

    path('password_reset_complete/',
    auth_views.PasswordResetCompleteView.as_view(template_name="password-reset-templates/reset_password_completed.html"),
    name="password_reset_complete"),

    path('password_change/',
    auth_views.PasswordChangeView.as_view(template_name="password-reset-templates/password_change.html"),
    name="password_change"),


    path('password_change_done/',
    auth_views.PasswordChangeDoneView.as_view(template_name="password-reset-templates/password_changed.html"),
    name="password_change_done"),
]

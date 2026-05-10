from django.urls import path
from . import views

app_name="mxauth"
urlpatterns = [
    path("login",views.mxlogin,name="login"),
    path("logout",views.mxlogout,name="logout"),
    path("register",views.register,name="register"),
    path("captcha",views.send_email_captcha,name="email_captcha")
]
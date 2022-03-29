from django.urls import path
from . import views

app_name = "main"

urlpatterns = [

	path("index/", views.IndexView, name="index"),
	path("", views.SignUpView, name="sign_up"),
	path("sign-in/", views.SignInView, name="sign_in"),

]
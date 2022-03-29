from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User

from django.core.mail import send_mail

from datetime import datetime
import datetime as dt
import requests


def IndexView(request):
	if request.method == "POST":
		pass


	else:
		data = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=metis-token&order=market_cap_desc&per_page=100&page=1&sparkline=true&price_change_percentage=1h").json()
		usd = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=usd-coin&order=market_cap_desc&per_page=100&page=1&sparkline=true&price_change_percentage=1h").json()
		btc  = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=bitcoin&order=market_cap_desc&per_page=100&page=1&sparkline=true&price_change_percentage=1h").json()
		context = {"data":data, "usd":usd, "btc":btc}

		return render(request, "main/index.html", context )



def SignInView(request):
	if request.method == "POST":
		pass


	else:
		context = {}

		return render(request, "main/sign_in.html", context )


def SignUpView(request):
	if request.method == "POST":
		pass


	else:
		context = {}

		return render(request, "main/sign_up.html", context )
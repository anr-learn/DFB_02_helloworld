# anr_pages/urls.py

from django.urls import path
from .views import homePageView

urlpatterns = [
	path("", homePageView, name="home"),
	]

### end ###

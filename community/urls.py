# community/urls.py
from django.conf.urls import url
from community import views
from community.views import coin_pann_community

urlpatterns = [
    url(r'^dcInside/', coin_pann_community),
    url(r'^$', views.HomePageView.as_view()),
]


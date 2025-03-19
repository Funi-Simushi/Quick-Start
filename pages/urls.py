from django.urls import path
from .views import HomePageView, AboutPageView, ContactPageView, MediaPageView

urlpatterns = [
    path('media/', MediaPageView.as_view(), name='media'),
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('', HomePageView.as_view(), name='home'),
]
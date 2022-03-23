from django.urls import path

from cryptoapp.views import CryptoWatching

app_name = 'cryptoapp'

urlpatterns = [
    path('', CryptoWatching.as_view(), name='index'),
]

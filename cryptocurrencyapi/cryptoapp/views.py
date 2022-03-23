import requests
from django.conf import settings
from django.shortcuts import render
from django.views.generic import TemplateView


class CryptoWatching(TemplateView):
    template_name = 'cryptoapp/index.html'

    def get_context_data(self, **kwargs):
        context = super(CryptoWatching, self).get_context_data(**kwargs)
        context['apidata'] = requests.get('https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page=1&sparkline=false').json()
        return context

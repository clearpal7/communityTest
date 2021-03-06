 # community/views.py
from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import JsonResponse
from crawler import CoinPannCrawler
from bs4 import BeautifulSoup
import re


# Create your views here.
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)


def coin_pann_community(request):
    page = request.GET.get('page')
    if page is None:
      page = 1
    raw_html = CoinPannCrawler.CoinPannCrawler(page)

    bsobj = BeautifulSoup(raw_html.get_html_text(), 'lxml')
    parsing_tr = bsobj.find_all("tr", {"class": re.compile("^bg")})
    content = bsobj.find_all("td", {"class": "title"})
    result = []
    for i in range(0, len(content)):
        title = content[i].get_text()
        url = content[i].find("a")
        if url.attrs["href"] is not None:
            url = url.attrs["href"]
        temp_dict = {"title": title, "url": url}
        result.append(temp_dict)
    return JsonResponse(result, safe=False)

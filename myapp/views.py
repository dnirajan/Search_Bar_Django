from django.db.models import Q
from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView, ListView

from .models import City


class HomePageView(TemplateView):
    template_name = 'home.html'


class SearchResultsView(ListView):
    model = City
    # context_object_name = 'city_list'
    template_name = 'search_results.html'

    def get_queryset(self):
        query = self.request.GET.get("q")
        city_list=City.objects.filter(
            Q(name__icontains=query) | Q(state__icontains=query)
        )
        return city_list
        # return City.objects.filter(name__icontains='Pok')

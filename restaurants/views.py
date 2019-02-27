from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View

from .models import RestaurantLocation
from .forms import RestaurantLocationCreateForm

# Create your views here.
class RestaurantListView(ListView):
    template_name = 'restaurants/diner.html'
    def get_queryset(self):
        print(self.kwargs)
        slug = self.kwargs.get("slug")
        if slug:
            queryset = RestaurantLocation.objects.filter(
                Q(category__iexact=slug) |
                Q(category__icontains=slug)
            )
        else:
            queryset = RestaurantLocation.objects.all()
        return queryset

class RestaurantDetailView(DetailView):
    queryset = RestaurantLocation.objects.all()

class RestaurantCreateView(LoginRequiredMixin, CreateView):
    form_class = RestaurantLocationCreateForm
    # login_url = '/login/'
    template_name = "restaurants/form.html"
    success_url = '/restaurants/'

    def form_valid(self, form): #form_valid is a std createview method that we are tweaking.
        instance = form.save(commit=False)
        instance.owner = self.request.user
        return super(RestaurantCreateView, self).form_valid(form)

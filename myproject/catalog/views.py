from .models import Product
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView


class HomeListView(ListView):
    model = Product
    template_name = 'product_list.html'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product/product_detail.html'


class ContactsTemplateView(TemplateView):
    template_name = 'contacts/contacts.html'




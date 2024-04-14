from django.urls import reverse_lazy

from .forms import ProductForm, VersionForm
from .models import Product, Version
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView


class HomeListView(ListView):
    model = Product
    template_name = 'product_list.html'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product/product_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = self.object
        active_versions = product.version_set.filter(current_version_indication=True)
        context['active_versions'] = active_versions
        return context


class ContactsTemplateView(TemplateView):
    template_name = 'contacts/contacts.html'


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:home')
    template_name = 'product/product_form.html'

    def form_valid(self, form):
        product = form.save(commit=False)
        product.save()
        selected_version = form.cleaned_data['version']
        selected_version.product = product
        selected_version.save()
        return super().form_valid(form)


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:home')
    template_name = 'product/product_form.html'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        if hasattr(self, 'object'):
            kwargs['product'] = self.object
        return kwargs

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        product = self.object
        active_versions = Version.objects.filter(product=product, current_version_indication=True)
        context_data['active_versions'] = active_versions
        return context_data

    def form_valid(self, form):
        product = form.save(commit=False)
        product.save()
        selected_version = form.cleaned_data['version']
        selected_version.product = product
        selected_version.save()
        return super().form_valid(form)


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:home')
    template_name = 'product/product_confirm_delete.html'


class VersionCreateView(CreateView):
    model = Version
    form_class = VersionForm
    template_name = 'version_create.html'
    success_url = reverse_lazy('catalog:home')




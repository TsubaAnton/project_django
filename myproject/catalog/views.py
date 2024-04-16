from django.forms import inlineformset_factory
from django.urls import reverse_lazy

from .forms import ProductForm, VersionForm
from .models import Product, Version
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView


class HomeListView(ListView):
    model = Product
    template_name = 'product_list.html'

    def get_queryset(self):
        return Product.objects.prefetch_related('version_set')


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product/product_detail.html'


class ContactsTemplateView(TemplateView):
    template_name = 'contacts/contacts.html'


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:home')
    template_name = 'product/product_form.html'

    # def form_valid(self, form):
    #     product = form.save(commit=False)
    #     product.save()
    #     return redirect('catalog:home')


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:home')
    template_name = 'product/product_form_formset.html'

    # def get_form_kwargs(self):
    #     kwargs = super().get_form_kwargs()
    #     return kwargs

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)

        if self.request.method == 'POST':
            context_data['formset'] = VersionFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = VersionFormset(instance=self.object)

        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']

        form_valid = super().form_valid(form)
        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        return form_valid


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:home')
    template_name = 'product/product_confirm_delete.html'


class VersionCreateView(CreateView):
    model = Version
    form_class = VersionForm
    template_name = 'version/version_form.html'
    success_url = reverse_lazy('catalog:home')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['version_form'] = self.get_form()
        return context_data



from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.forms import inlineformset_factory
from django.urls import reverse_lazy
from django.core.exceptions import PermissionDenied
from .forms import ProductForm, VersionForm, ProductModeratorForm
from .management.commands.mail import send_order_email
from .models import Product, Version, Category
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView

from .services.category import all_category


class HomeListView(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'product_list.html'

    def get_queryset(self):
        return Product.objects.prefetch_related('version_set')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        is_moderator = user.groups.filter(name='moderators').exists()
        context['is_moderator'] = is_moderator
        return context


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'product/product_detail.html'


class ContactsTemplateView(LoginRequiredMixin, TemplateView):
    template_name = 'contacts/contacts.html'


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:home')
    template_name = 'product/product_form.html'

    def form_valid(self, form):
        instance = form.save()
        instance.author = self.request.user
        send_order_email()

        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:home')
    template_name = 'product/product_form_formset.html'

    # def get_form_kwargs(self):
    #     kwargs = super().get_form_kwargs()
    #     return kwargs

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        user = self.request.user
        is_moderator = user.groups.filter(name='moderators').exists()
        if is_moderator:
            context_data['show_version_form'] = False  # Устанавливаем флаг как False для модераторов
        else:
            VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
            if self.request.method == 'POST':
                context_data['formset'] = VersionFormset(self.request.POST, instance=self.object)
            else:
                context_data['formset'] = VersionFormset(instance=self.object)
            context_data['show_version_form'] = True  # Устанавливаем флаг как True для остальных пользователей
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data.get('formset')

        form_valid = super().form_valid(form)
        if formset is not None and formset.is_valid():
            formset.instance = self.object
            formset.save()
        return form_valid

    def test_func(self):
        user = self.request.user
        obj = self.get_object()

        is_author = user = obj.author

        is_moderator = user.groups.filter(name='moderators').exists()
        # return user.groups.filter(name='moderators').exists() or user == obj.author
        return is_author or is_moderator

    def get_form_class(self):
        user = self.request.user
        if user == self.object.author:
            return ProductForm
        # elif user.has_perm('catalog.can_change_description_product') and user.has_perm('catalog.can_change_category_product'):
        elif user.groups.filter(name='moderators').exists():
            return ProductModeratorForm
        else:
            raise PermissionDenied


class ProductDeleteView(LoginRequiredMixin, DeleteView):
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


class CategoryListView(ListView):
    model = Category
    template_name = 'category/category_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['categories'] = all_category()
        return context
class CategoryListView(ListView):
    model = Category
    template_name = 'category/category_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['categories'] = all_category()
        return context

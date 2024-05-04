from django.urls import path
from django.views.decorators.cache import cache_page

from .apps import CatalogConfig
from .views import HomeListView, ProductDetailView, ContactsTemplateView, ProductCreateView, ProductUpdateView, ProductDeleteView, CategoryListView


app_name = CatalogConfig.name

urlpatterns = [
    path('', HomeListView.as_view(), name='home'),
    path('contacts/', ContactsTemplateView.as_view(), name='contacts'),
    path('product/<int:pk>/', cache_page(60)(ProductDetailView.as_view()), name='product_detail'),
    path('product/create', ProductCreateView.as_view(), name='product_create'),
    path('product/<int:pk>/update', ProductUpdateView.as_view(), name='product_update'),
    path('product/delete/<int:pk>', ProductDeleteView.as_view(), name='product_confirm_delete'),
    path('category/', CategoryListView.as_view(), name='category')
]

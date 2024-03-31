from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import HomeListView, ProductDetailView, ContactsTemplateView

app_name = CatalogConfig.name

urlpatterns = [
    path('', HomeListView.as_view(), name='home'),
    path('contacts/', ContactsTemplateView.as_view(), name='contacts'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
]

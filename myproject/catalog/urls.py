from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import HomeListView, ProductDetailView, ContactsTemplateView, ProductCreateView, ProductUpdateView, ProductDeleteView, VersionCreateView

app_name = CatalogConfig.name

urlpatterns = [
    path('', HomeListView.as_view(), name='home'),
    path('contacts/', ContactsTemplateView.as_view(), name='contacts'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('product/create', ProductCreateView.as_view(), name='product_create'),
    path('product/<int:pk>/update', ProductUpdateView.as_view(), name='product_update'),
    path('product/delete/<int:pk>', ProductDeleteView.as_view(), name='product_confirm_delete'),
    path('version/create', VersionCreateView.as_view(), name='version_create')
]

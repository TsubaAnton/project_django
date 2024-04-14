from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms

from .models import Product, Version


class ProductForm(forms.ModelForm):
    version = forms.ModelChoiceField(queryset=Version.objects.all(), empty_label=None)

    class Meta:
        model = Product
        fields = ('name', 'description', 'image', 'category', 'price',)

    def __init__(self, *args, **kwargs):
        product = kwargs.pop('product', None)
        super(ProductForm, self).__init__(*args, **kwargs)
        if product:
            self.fields['version'].queryset = Version.objects.filter(product=product)

    def clean_name(self):
        cleaned_data = self.cleaned_data.get('name')
        if cleaned_data.lower() in (
                'казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'обман', 'полиция',
                'радар'):
            raise forms.ValidationError(f"Нельзя использовать слово {cleaned_data} в названии")
        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data.get('description')
        if cleaned_data.lower() in (
                'казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'обман', 'полиция',
                'радар'):
            raise forms.ValidationError(f"Нельзя использовать слово {cleaned_data} в описании")
        return cleaned_data


class VersionForm(forms.ModelForm):
    class Meta:
        model = Version
        fields = ('number', 'name', 'current_version_indication')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['number'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter version number'
        })
        self.fields['name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter version name'
        })
        self.fields['current_version_indication'].widget.attrs.update({
            'class': 'form-check-input',
            'id': 'current_version_checkbox'
        })

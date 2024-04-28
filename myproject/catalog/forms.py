from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout
from django import forms

from .models import Product, Version


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('name', 'description', 'image', 'category', 'price', 'publication_sign')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'name',
            'description',
            'image',
            'category',
            'price',
            'publication_sign',
            Submit('submit', 'Submit', css_class='btn-primary')
        )

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


class ProductModeratorForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('description', 'category')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'description',
            'category',
            Submit('submit', 'Submit', css_class='btn-primary')
        )

    def clean_description(self):
        cleaned_data = self.cleaned_data.get('description')
        if cleaned_data.lower() in (
                'казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'обман', 'полиция',
                'радар'):
            raise forms.ValidationError(f"Нельзя использовать слово {cleaned_data} в описании")
        return cleaned_data


class VersionForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'product',
            'number',
            'version_name',
            'current_version_indication',
            Submit('submit', 'Submit', css_class='btn-primary')
        )

    class Meta:
        model = Version
        fields = '__all__'

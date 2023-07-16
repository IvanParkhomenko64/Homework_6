from django import forms

from catalog.models import Product, Version


class ProductForm(forms.ModelForm):
    banned_titles = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            if field_name == 'version_is_active':
                continue
            field.widget.attrs['class'] = 'form-control'

    def clean_name(self):
        cleaned_data = self.cleaned_data['name']
        for name in ProductForm.banned_titles:
            if name == cleaned_data.lower():
                raise forms.ValidationError('Название содержит запрещённое слово')
        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data['description']
        for name in ProductForm.banned_titles:
            if name in cleaned_data.lower():
                raise forms.ValidationError('Описание содержит запрещённое слово')
        return cleaned_data


class VersionForm(forms.ModelForm):

    class Meta:
        model = Version
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            if field_name == 'version_is_active':
                continue
            field.widget.attrs['class'] = 'form-control'


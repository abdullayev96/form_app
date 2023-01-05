from django import forms
from .models import Customer

class CustomersForm(forms.ModelForm):   #### new 1       modelni xusisiytiga qarab html formlar yaratib beradi
    class Meta:   #### new 2
        model=Customer  ##### new 3
        fields="__all__"    ##### new 4  ["first_name"]          fields   modeldan qaysi ustunlarni olish uchun ishlatamz




from django import forms

from .models import RestaurantLocation
from .validators import validate_category

class RestaurantLocationCreateForm(forms.ModelForm):
   # email = forms.EmailField()
   # category = forms.CharField(required=False, validators=[validate_category])
   class Meta:
       model = RestaurantLocation
       fields = ['name', 'location', 'category']


   def clean_name(self):
        name = self.cleaned_data.get("name")
        if name == "Hello":
            raise forms.ValidationError("Not a valid name")
        return name

   # def clean_email(self):
   #     email = self.cleaned_data.get("email")
   #     if '.edu' in email:
   #         raise forms.ValidationError("We don't not accept edu emails")
   #     return email

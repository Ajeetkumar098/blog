from django import forms
from blog_app.models import add,contact_us,profileimage

class add_form(forms.ModelForm):
    class Meta:
        model = add
        fields ='__all__'


class contact_us_form(forms.ModelForm):
    class Meta:
        model = contact_us
        fields = '__all__'

class profileimageform(forms.ModelForm):
    class Meta:
        model = profileimage
        fields = '__all__'

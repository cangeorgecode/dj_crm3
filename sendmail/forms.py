from django import forms

class ContactForm(forms.Form):
    Name = forms.CharField(required=True)
    Email = forms.EmailField(required=True)
    Message = forms.CharField(widget=forms.Textarea)
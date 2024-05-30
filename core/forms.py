from django import forms
from .models import *
from django.forms import FileField, Form

class AddRecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ('full_name', 'biz_name', 'address', 'email', 'phone', 'category')

    def __init__(self, *args, **kwargs):
        super(AddRecordForm, self).__init__(*args, **kwargs)

        self.fields['full_name'].label = ''
        self.fields['full_name'].widget.attrs['class'] = 'form-control'
        self.fields['full_name'].widget.attrs['placeholder'] = 'Full Name'
        self.fields['full_name'].help_text = ''

        self.fields['biz_name'].label = ''
        self.fields['biz_name'].widget.attrs['class'] = 'form-control'
        self.fields['biz_name'].widget.attrs['placeholder'] = 'Business Name'
        self.fields['biz_name'].help_text = ''

        self.fields['address'].label = ''
        self.fields['address'].widget.attrs['class'] = 'form-control'
        self.fields['address'].widget.attrs['placeholder'] = 'Address'
        self.fields['address'].help_text = ''

        self.fields['email'].label = ''
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['email'].help_text = ''

        self.fields['phone'].label = ''
        self.fields['phone'].widget.attrs['class'] = 'form-control'
        self.fields['phone'].widget.attrs['placeholder'] = 'Phone'
        self.fields['phone'].help_text = ''

        self.fields['category'].label = ''
        self.fields['category'].widget.attrs['class'] = 'form-select'
        self.fields['category'].widget.attrs['placeholder'] = 'Phone'
        self.fields['category'].help_text = ''
   

class UploadForm(Form):
    records_file = FileField()

    def __init__(self, *args, **kwargs):
        super(UploadForm, self).__init__(*args, **kwargs)

        self.fields['records_file'].label = 'Accepts csv file only'
        self.fields['records_file'].widget.attrs['class'] = 'form-control'
        self.fields['records_file'].widget.attrs['placeholder'] = ''
        self.fields['records_file'].help_text = ''

class AddTodoForm(forms.ModelForm):
    due_date = forms.DateField(widget = forms.SelectDateWidget())

    class Meta:
        model = Todos
        fields = ('todos', 'due_date',)
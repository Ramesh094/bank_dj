from django import forms
from .models import Accounts
class AccountForm(forms.Form):
    model = Accounts
    name = forms.CharField(required=True)
    dob = forms.DateField(required=True)
    mobile = forms.IntegerField(required=True)
    aadhar = forms.IntegerField(required=True)
# just checking can i change the code via github
# class AccountForm(forms.ModelForm):
#     class Meta:
#         model = Accounts
#         fields = ['acc_name', 'aadhar', 'mobile', 'dob', 'bank_acc']


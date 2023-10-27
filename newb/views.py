from django.shortcuts import render, redirect
from .models import Accounts
from .forms import AccountForm
from django.urls import reverse

# Create your views here.

def cover(request):
    return render(request, 'home.html')

# def create_employee(request):
#     print('function')
#     if request.method == 'POST':
#         form = AccountForm(request.POST)
#         if form.is_valid():
#             acc_num = form.cleaned_data.get('aadhar')  # Get the aadhar number
#             # Set the initial value for the bank_acc field
#             instance = Accounts(bank_acc=acc_num)
#             instance.save()  # Save the form data to your model
#             return redirect(reverse('success.html'))
#         else:
#             print(form.errors)
#             # print('return')
#             # return render(request, 'create.html', {'form': form})
#     else:
#         form = AccountForm()
#     return render(request, 'create.html', {'form': form})

def create_employee(request):
    if request.method == 'POST':
        form = AccountForm(request.POST)
        if form.is_valid():
            acc_num = form.cleaned_data.get('aadhar')

            new_account = Accounts(name=form.cleaned_data['name'], dob=form.cleaned_data['dob'], mobile=form.cleaned_data['mobile'], aadhar=acc_num, bank_acc=acc_num)
            new_account.save()
            return redirect(reverse('success'))
    else:
        form = AccountForm()
    return render(request, 'create.html', {'form': form})

def success_view(request):
    return render(request, 'success.html')
from django.db import models
from django.core.validators import RegexValidator
# Create your models here.
# class Accounts(models.Model):
#     class Meta:
#         app_label = 'newb'
#
#     acc_name = models.CharField(max_length=20)
#     mobile = models.IntegerField(
#         max_length=10,
#         validators=[
#             RegexValidator(
#                 regex=r'^\d{10}$',
#                 message='Your mobile number should be 10 digits long'
#             )
#         ]
#     )
#     aadhar = models.IntegerField(
#         max_length=12,
#         validators=[
#             RegexValidator(
#                 regex=r'^\d{12}$',
#                 message='Your Aadhar number should be 12 digits long'
#             )
#         ]
#     )
#     dob = models.DateField()
#     bank_acc = models.IntegerField()

class Accounts(models.Model):
    name = models.CharField(max_length=255)
    dob = models.DateField()
    mobile = models.CharField(max_length=20)  # You may want to use CharField for a phone number
    aadhar = models.CharField(max_length=12)  # Assuming Aadhar is a 12-digit number
    bank_acc = models.BigIntegerField(max_length=14)
    def __str__(self):
        return self.name
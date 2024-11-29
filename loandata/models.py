from django.db import models

class loandata(models.Model):
     phone = models.CharField(max_length=15)
     name = models.CharField(max_length=100)
     sur_name = models.CharField(max_length=100)
     email = models.EmailField()
     pancard = models.CharField(max_length=20)
     date_of_birth = models.DateField(null=True, blank=True)
     monthly_income = models.FloatField(null=True, blank=True)
     pincode = models.CharField(max_length=10)
     education = models.CharField(max_length=100)
     empoyement_type = models.CharField(max_length=100)
     adhar = models.CharField(max_length=20)
     address = models.CharField(max_length=255)
     occupation = models.CharField(max_length=100)
     reference = models.CharField(max_length=100)
     ref_contact = models.CharField(max_length=15)
     f_name = models.CharField(max_length=100)
     m_status = models.CharField(max_length=100)
     f_contact = models.CharField(max_length=15)

# Create your models here.

from django.contrib import admin
from loandata.models import loandata
# Register your models here.
class LoanAdmin(admin.ModelAdmin):
     list_display=('phone','name','sur_name','email','pancard','monthly_income','date_of_birth','pincode','education','empoyement_type','occupation','adhar','address',
                   'reference','ref_contact','f_name','f_contact','m_status')
admin.site.register(loandata,LoanAdmin)
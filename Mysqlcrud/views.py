from django.shortcuts import redirect, render
from .forms import MyRegisterForm
from django.contrib import messages
from .models import RegisterForm

def home(request):
    data = RegisterForm.objects.all()
    if (data !=''):
        return render(request, "home.html", {'data': data})
    else:
        return render(request,"home.html")

def insert(request):
    if request.method == 'POST':
        form = MyRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successfully completed")
            return redirect("home")
        else:
            messages.error(request, "Form is not valid")
    else:
        form = MyRegisterForm()
    return render(request, "register.html", {'form': form})

def update(request,id):
    data=RegisterForm.objects.get(id=id)
    if request.method=='POST':
        FirstName=request.POST['FirstName']
        LastName=request.POST['LastName']
        Father_Name=request.POST['Father_Name']
        
        data.FirstName=FirstName
        data.LastName=LastName
        data.Father_Name=Father_Name
        data.save()
        messages.success(request,"update successfully completed")
        return redirect("home")
    return render(request,"update.html",{'data':data})

def delete(request,id):
    data=RegisterForm.objects.get(id=id)
    data.delete()
    messages.success(request,"Record deleted successfully")
    return redirect("home")


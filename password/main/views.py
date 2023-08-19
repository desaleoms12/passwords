from django.shortcuts import render,HttpResponse,redirect
from .models import Password
from django.db.models import Q
from .form import PasswordForm
# Create your views here.
def home(request):
    password=Password.objects.all()
    password_form=PasswordForm()

    context={
        'password':password,
        'password_form':password_form
    }

    return render(request, "main/home.html",context)

def query(request):
    if request.method == "POST":
        query=request.POST['query']
        
        q_pass = Password.objects.filter(
                Q(account__icontains=query) |
                Q(email__icontains=query)
        )
        print(q_pass)

        context={
        'q_pass':q_pass
        }
    return render(request, "main/q.html",context)


def add(request):
    if request.method=="POST":
        account=request.POST['account']
        email=request.POST['email']
        password=request.POST['password']
        
        password_entry=Password(account=account,email=email,password=password)
        password_entry.save()

        return redirect('home')
    return HttpResponse("HELLO")
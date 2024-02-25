from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import add_data

# Create your views here.
def index(request):
    return render(request,'index.html')


def welcome(request):
    if request.method == 'POST':
        option = request.POST.get('option')
        if option == 'login':
            return redirect('login')  # Assuming you have a 'login' URL pattern
        elif option == 'signup':
            return redirect('form')  # Assuming you have a 'form' URL pattern

    return render(request, 'welcome.html')



def languages(request):
    return render(request, 'languages.html')

def chat (request):
    return render(request, 'chat.html')



def form(request):
    if request.method=='POST':
        name=request.POST.get('name')
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        address=request.POST.get('address')
        age=request.POST.get('age')
        password=request.POST.get('password')
        add_data(name=name,phone=phone,mail=email,address=address,age=age,password=password).save()
        return render(request,'index.html')
    
    else:
        return render(request,'form.html')




def login(request):
    if request.method=='POST':
        name=request.POST.get('name')
        print(name)
        password=request.POST.get('password')
        cr=add_data.objects.filter(name=name,password=password)
        if cr:
            userd=add_data.objects.get(name=name,password=password)
            name=userd.name
            password=userd.password
            request.session['name']=name
            return render(request,'index.html')
        else:
            return render(request,'login.html')
    else:
        return render(request,'login.html')


def userprofile(request):
    name=request.session['name']
    cr=add_data.objects.get(name=name)
    if cr:
        user_info={
            'name':cr.name,
            'phone':cr.phone,
            'mail':cr.mail,
            'address':cr.address,
            'age':cr.age,
        }
        return render(request,'userprofile.html',user_info)
    else:
        return render(request,'userprofile.html')


def update(request):
    name=request.session['name']
    cr=add_data.objects.get(name=name)
    if cr:
        user_info={
            'name':cr.name,
            'phone':cr.phone,
            'mail':cr.mail,
            'address':cr.address,
            'age':cr.age,
            }
        return render (request,'update.html',user_info)
    else:
        return render(request,'update.html')

def proupdate(request):
    name=request.session['name']
    if request.method=='POST':
        name=request.POST.get('name')
        phone=request.POST.get('phone')
        mail=request.POST.get('mail')
        age=request.POST.get('age')
        address=request.POST.get('address')

        data=add_data.objects.get(name=name)
        data.name=name
        data.mail=mail
        data.phone=phone
        data.address=address
        data.age=age

        data.save()
        return redirect('userprofile')
    else:
        return render(request,'update.html')

 



      

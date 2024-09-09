from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Customer

# Create your views here.
def login(request):
   if request.method == 'POST':
      username = request.POST.get('username')
      password=request.POST.get('password')
      if Customer.objects.filter(Username=username,Password=password).exists():
         userdetail=Customer.objects.get(Username=request.POST['username'],Password=password)
         if userdetail.Password==request.POST['password']:
            request.session['uid']=userdetail.id 
            return redirect(userhome)
         else:
            return render (request,'login.html')
      else:
         return render(request,'login.html',{'message':'Invalid Username or password'})
   else:
      return render(request,'login.html') 


def register(request):
    if request.method=='POST':
      name=request.POST['name']
      email= request.POST['email'] 
      address= request.POST['address'] 
      image= request.FILES['image']
      username=request.POST['username']
      if Customer.objects.filter(Username=username).exists():
         return render(request,'registration.html',{'message':'username already exist'})
      password1=request.POST['password1']
      password2=request.POST['password2']
      if password1 !=password2:
         return render(request,'registration.html',{'message':'passwords do not match'})
      else:
        data=Customer.objects.create(Name=name,Email=email,Address=address,Image=image,Username=username,Password=password1)
      data.save()
      return HttpResponse("successfull")
    else:
       return render(request,'registration.html') 
    


def userhome(request):
   tem=request.session['uid'] 
   data =Customer.objects.get(id = tem)
   return render(request,'userhome.html',{'data':data})   

def edit(request,id):
  data=Customer.objects.get(id=id) 
  if request.method=='POST':
   data.Name=request.POST['name']
   data.Email=request.POST['email']
   data.Address=request.POST['address']
   if 'image' in request.FILES:
      data.Image =request.FILES['image']
   data.save()
   return redirect(userhome)
  else:
     return render(request,'edit.html',{'data':data})


def logout(request):
   session_keys=list(request.session.keys())
   for key in session_keys:
      del request.session[key]
   return redirect(login)   
  
def login(request):
   if request.method=='POST':
      username=request.POST['username']
      password=request.POST['password']
      if Customer.objects.filter(Username=username,Password=password).exists():
         userdetails=Customer.objects.get(Username=request.POST['username'],Password=password)
         if userdetails.Password==request.POST['password']:
            request.session['uid']=userdetails.id
            return redirect(userhome)
         else:
            return render(request,'login.html')
      else:
         return render(request,'login.html',{'message':'Invalid username or password'}) 
   else:
      return render(request,'login.html')      

             




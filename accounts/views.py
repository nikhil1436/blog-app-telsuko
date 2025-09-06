from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
def login(request):
     if request.method=="POST":
          username=request.POST['username']
          password=request.POST['password']

          user=auth.authenticate(request,username=username,password=password)
          if user is not None:
               auth.login(request,user)
               return redirect('/')
          else:
               messages.error(request,"invlaid credentails")
               return render(request,'login.html')

     else:
          return render(request,'login.html')
def register(request):
    if request.method=='POST':
        first_name= request.POST['first_name']
        last_name= request.POST['last_name']
        username= request.POST['username']
        email= request.POST['email']
        password1= request.POST['password1']
        password2= request.POST['password2']

        if password1!=password2:
            messages.error(request, "Passwords do not match.")
            return render(request, 'register.html', {
                'first_name': first_name,
                'last_name': last_name,
                'username': username,
                'email': email,
            })
        if User.objects.filter(username=username).exists():
            messages.error(request,"username taken")
            
            return render(request,'register.html',{
                    'first_name':first_name,
                    'last_name':last_name,
                    'email':email,
                        })
        if User.objects.filter(email=email).exists():
                messages.error(request,"email exists")
                return render(request,'register.html',{
                    'first_name':first_name,
                    'last_name':last_name,
                    'username':username,
                })

            
        
            
        user=User.objects.create_user(username=username, password=password1, first_name=first_name,last_name=last_name,email=email)
        #user.save()
        
        return redirect ('login')
            

    
    return render(request,'register.html')
def logout(request):
     auth.logout(request)
     return redirect('/')
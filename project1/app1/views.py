from django.shortcuts import render
from .models import userModel
from django.http import JsonResponse
# Create your views here.

def create(request):
    print('working......................')
    if request.method == 'GET': 
        print(request.GET.get("name")) # get the value of name
        name = request.GET['name']
        email = request.GET['email']
        userModel.objects.create(name =name ,email = email)
       
        return JsonResponse({"status":True})
    return JsonResponse({"status":False})

def home(request):
    return render(request,'home.html')


def show(request):
    data = list(userModel.objects.all().values())
    return JsonResponse(data,safe=False)

def ashow(request):
     data=list(userModel.objects.all().values())
     return JsonResponse(data, safe=False)
 

def delete1(request):
    
    id=request.GET['did']
    print(id)
    obj=userModel.objects.get(id=id)
    obj.delete()
    return JsonResponse({"status":True})

def update1(request):
    print('working...........')
    id=request.GET['uid']
    obj=list(userModel.objects.filter(id=id).values())
    return JsonResponse(obj,safe=False)


def update2(request):
    uuid=request.GET['uuid']
    data=userModel.objects.filter(id=uuid).first()
    print(data)
    name=request.GET["uname"]
    email=request.GET["uemail"]
    data.update(name=name,email=email)
    return JsonResponse({"status":True})
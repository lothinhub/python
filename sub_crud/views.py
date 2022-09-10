
from email.mime import image
from django.shortcuts import redirect
from multiprocessing import context
from django.shortcuts import render
from sub_crud.models import Employees

def index(request):
    emp =Employees.objects.all()
    context={
        'employees': emp,
        
    }
    return render(request, 'index.html',context)



def add(request):
    if request.method == 'POST':
        if len(request.FILES) != 0:
            image = request.FILES['image']
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone= request.POST.get('phone')
        emp=Employees(
            # image=image,
            name=name,
            email= email,
            address= address,
            phone= phone,
        )
        emp.save()
        return redirect('home')
    return render(request, 'index.html')

def edit(request):
    emp=Employees.objects.all()
    context={
        'employees':emp
    }
    return render(request, 'index.html',context)

def update(request,id):
    if request.method == 'POST':
        image =request.POST.get('image')
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone= request.POST.get('phone')
        emp=Employees(
            id=id,
            image= image,
            name=name,
            email= email,
            address= address,
            phone= phone,
        )
        emp.save()
        return redirect('home')
    return render(request, 'index.html',context)

def delete(request,id):
    emp = Employees.objects.filter(id=id)
    emp.delete()
    context = {'employees':emp,}
    return redirect('home')
from django.shortcuts import render
from app1.models import Vihicle
from app1.form import VihicleForm


# Create your views here.

def home(request):
    b = Vihicle.objects.all
    return render(request, 'home.html', {'v': b})

def viewvihicle(request,k):
    b=Vihicle.objects.get(id=k)
    return render(request,'viewvihicle.html',{'b1':b})


def add_vihicle(request):
    if request.method == 'POST':
        m = request.POST['m']
        f = request.POST['f']
        c = request.POST['c']
        n = request.POST['n']
        b= Vihicle.objects.create(model_type=m,fuel=f,color=c,number=n)
        b.save()
        return home(request)
    return render(request,'add_vihicle.html')


def delete(request,k):
    b=Vihicle.objects.get(id=k)
    b.delete()
    return home(request)


def update(request,k):
    b=Vihicle.objects.get(id=k)
    if (request.method == "POST"):
        form = VihicleForm(request.POST, request.FILES, instance=b)
        if form.is_valid():
            form.save()
            return home(request)

    form = VihicleForm(instance=b)
    return render(request,'update.html',{'f':form})






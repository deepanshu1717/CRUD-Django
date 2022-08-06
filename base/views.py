from django.shortcuts import render
from django.shortcuts import get_object_or_404,redirect

# Create your views here.

from . models import Main
from . forms import MainForm


def Home(request):
    return render(request, "home.html")



def Create(request):
    context = {}
    form = MainForm(request.POST or None)
    if form.is_valid():
       form.save()

    context['form']=form

    return render(request, "create.html",context)

def List_View(request):
    context = {}
    context["dataset"] = Main.objects.all()

    return render(request, "listview.html", context)



def Detail_View(request,id):
    context = {}
    context['data'] = Main.objects.get(id=id)
    return render(request,"detail.html",context)




def Update_View(request,id):
    context = {}
    obj = get_object_or_404(Main ,id=id)

    form = MainForm(request.POST or None, instance = obj)
    if form.is_valid():
       form.save()
       return redirect("listview")
    context["form"]= form
    
    return render(request, "update.html", context)



def Delete_View(request,id):
    context = {}
    obj = get_object_or_404(Main,id=id)

    if request.method == "POST":
        obj.delete()
        return redirect("listview")
 
    return render(request, "delete.html", context)

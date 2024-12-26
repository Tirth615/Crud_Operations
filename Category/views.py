from django.shortcuts import render, redirect

from Category.models import Category


# Create your views here.

def index(request):
    return render(request, 'Index.html')

def addcategory(request):

    return render(request,'addcategory.html')

def insertcategory(request):
    category_vo = Category()
    category_vo.category_name = request.POST['category_name']
    category_vo.category_description = request.POST['category_description']
    category_vo.save()
    return render(request,'Index.html')

def viewcategory(request):
    category_vo = Category.objects.all()
    return render(request,'viewcategory.html',{'category_vo':category_vo})

def editcategory(request):
    category_id = request.GET.get("category_id")
    category_vo_list = Category.objects.filter(category_id =
                                             category_id).all()
    return render(request,"editCategory.html",{"category_vo_list": category_vo_list})

def updatecategory(request):
    category_vo = Category()
    category_vo.category_id = request.POST.get("category_id")
    category_vo.category_name = request.POST.get("category_name")
    category_vo.category_description = request.POST.get("category_description")
    category_vo.save()
    return redirect(viewcategory)


def deletecategory(request):
    category_vo = Category()
    category_vo.category_id = request.GET.get('category_id')
    category_vo.delete()
    return redirect(viewcategory)

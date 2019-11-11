from django.shortcuts import render, HttpResponse, redirect
from .models import *

def shows_new(request):
    context= {
        "all_the_shows": Shows.objects.all()
    }
    return render(request, "shows_new.html", context)

def add_show(request):
    print("Someone added a show")
    new_show = Shows.objects.create(title=request.POST['title'], network=request.POST['network'], release_date=request.POST['release_date'], description=request.POST['description'])
    return redirect(f"/show_page/{new_show.id}")

def show_page(request, show_id):
    context = {
        'show': Shows.objects.get(id=show_id)
    }
    return render(request, "show_page.html", context)

def shows(request):
    context= {
        "all_the_shows": Shows.objects.all()
    }
    return render(request, "shows.html", context)

def show_edit(request, show_id):
    context= {
        "all_the_shows": Shows.objects.all(),
        "show": Shows.objects.get(id=show_id)
    }
    return render(request, "show_edit.html", context)

def edit_show(request, show_id):
    print("Someone edited a show")
    show = Shows.objects.get(id=show_id)
    show.title=request.POST['title'] 
    show.network=request.POST['network']
    show.release_date=request.POST['release_date']
    show.description=request.POST['description']
    show.save()
    return redirect(f"/show_page/{show_id}")


def delete(reqest, show_id):
    show = Shows.objects.get(id=show_id)
    show.delete()
    return redirect('/shows')


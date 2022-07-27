from ast import Return
from django.shortcuts import render, get_object_or_404, HttpResponse, redirect
from home.models import Contact
from datetime import datetime
import requests
# Create your views here.


def index(request):
    return render(request, "users/index.html")


def allusers(request):
    # for delete coustomer record
    if request.method == 'POST':
        id = request.POST.get('user_id')
        obj = get_object_or_404(Contact, id=id)
        obj.delete()

    users = Contact.objects.values()
    all_user = {
        "users": users
    }
    # print(all_user[users])
    return render(request, "users/allusers.html", all_user)


def editUser(request, id):
    if request.method == 'POST':
        obj = get_object_or_404(Contact, id=id)
        obj.name = request.POST.get('name')
        obj.email = request.POST.get('email')
        obj.phone = request.POST.get('phone')
        obj.message = request.POST.get('message')
        obj.date = datetime.today()
        obj.save()
        return redirect('allusers')
    context = {}
    # context['user_data'] = Contact.objects.get(id=id)
    context['user_data'] = get_object_or_404(Contact, id=id)
    return render(request, 'users/useredit.html', context)


def allposts(request, userId=0):
    if userId != '0':
        params = {
            "id": userId
        }
        post = requests.post(
            'https://jsonplaceholder.typicode.com/posts/', params).json()
        context = {
            'post': post
        }
        return render(request, 'users/view_post.html', context)
    posts = requests.get('https://jsonplaceholder.typicode.com/posts').json()
    context = {
        'allPosts': posts
    }
    return render(request, 'users/all_posts.html', context)

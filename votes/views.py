from django.shortcuts import render , redirect
from .models import videos , voters
from django.contrib.auth.models import User , auth
from django.contrib.auth.decorators import login_required
# Create your views here.

def login1(request):
    if request.method=="POST":
        name = request.POST.get('name','')
        number = request.POST.get('number','')
        user_main=User.objects.create_user(username=name,password=number)
        user_main.save()
        user=voters(name=name,number=number)
        user.save()
        userlogin = auth.authenticate(username=name , password=number)
        if user:
            auth.login(request,userlogin)
            return redirect("index")
        else:
            err = 'Try again!'
            return render(request,"login1.html",{'err':err})
    return render(request,"login1.html")

@login_required(login_url="/")
def index(request):
    post = videos.objects.all()
    user_info = voters.objects.get(name=request.user)
    ifvoted=user_info.voted
    return render(request,"index.html",{'post':post,'ifvoted':ifvoted})

@login_required(login_url="/")
def indexx(request,id_name):
    ifvoted=None
    post = videos.objects.all()
    user_info = voters.objects.get(name=request.user)
    if request.method == "POST":
        user_info.voted=True
        ifvoted = True
        user_info.save()
        video_info = videos.objects.get(id_name=id_name)
        video_info.votes = int(video_info.votes) + 1
        video_info.save()
        return render(request,"index.html",{'post':post,'ifvoted':ifvoted})

    return redirect("index")

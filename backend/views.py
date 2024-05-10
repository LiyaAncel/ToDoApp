from django.shortcuts import render,redirect
from backend.models import taskDB, reportDB
from frontend.models import submissionDB
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def Home_page(request):
    return render(request,"Home.html")


def save_task(request):
    if request.method=="POST":
        t = request.POST.get('task')
        e = request.POST.get('emp')
        des = request.POST.get('des')
        dt = request.POST.get('date')
        obj=taskDB(Task_Title=t,Employee=e,Description=des,Due_date=dt)
        obj.save()
        messages.success(request, "Task added successfully..!")
        return redirect(Home_page)

def display_tasks(request):
    data=taskDB.objects.all()
    return render(request,"Tasks.html",{'data':data})

def delete_task(request,tid):
    x = taskDB.objects.filter(id=tid)
    x.delete()
    messages.error(request, "Task removed..!")
    return redirect(display_tasks)

def edit_task(request,tid):
    tdata = taskDB.objects.get(id=tid)
    return render(request,"edit_task.html", {'tdata':tdata})

def update_task(request,tid):
    if request.method=="POST":
        t = request.POST.get('task')
        e = request.POST.get('emp')
        des = request.POST.get('des')
        dt = request.POST.get('date')
        taskDB.objects.filter(id=tid).update(Task_Title=t,Employee=e, Description=des, Due_date=dt)
        messages.success(request, "Task Updated successfully..!")
        return redirect(display_tasks)

def login_page(request):
    return render(request,"adminloginpage.html")

def Admin_login_fn(request):
    if request.method == "POST":
        un = request.POST.get('uname')
        pwd = request.POST.get('passwd')
        if User.objects.filter(username__contains=un).exists():
            x = authenticate(username=un, password=pwd)
            if x is not None:
                login(request,x)
                request.session['username']=un
                request.session['password']=pwd
                messages.success(request, "Welcome..!")
                return redirect(Home_page)
            else:
                messages.error(request, "Incorrect Password..!")
                return redirect(login_page)
        else:
            messages.error(request, "Invalid Username..!")
            return redirect(login_page)

def AdminLogout_fn(request):
    del request.session['username']
    del request.session['password']
    messages.warning(request, "Logged Out..!")
    return redirect(login_page)


def task_submissions(request):
    sub = submissionDB.objects.all()
    return render(request,"submissions.html",{'sub':sub})

def delete_submissions(request,title):
    sub = submissionDB.objects.get(Task=title)
    sub.delete()
    messages.error(request, "Submission removed..!")
    return redirect(task_submissions)

def task_verification(request,title):
    title = submissionDB.objects.get(Task=title)
    return render(request,"opensub_task.html",{'title':title})

def save_report(request):
    if request.method == "POST":
        t = request.POST.get('task')
        e = request.POST.get('emp')
        r = request.POST.get('report')
        if reportDB.objects.filter(Task_Title=t).exists():
            return render(request,"already_verified.html")
        else:
            obj = reportDB(Task_Title=t, Employee=e, Result=r)
            obj.save()
            messages.success(request, "Task verification is complete..!")
            return redirect(task_submissions)
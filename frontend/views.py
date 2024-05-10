from django.shortcuts import render,redirect
from backend.models import taskDB, reportDB
from frontend.models import registerDB, submissionDB
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def User_Home_Page(request):
    return render(request,"User_Home.html")

def All_Tasks_users(request):
    data = taskDB.objects.all()
    return render(request,"all_tasks.html",{'data':data})

def user_login_page(request):
    return render(request, "userlogin.html")

def user_reg_page(request):
    return render(request, "userregistration.html")

def save_reg(request):
    if request.method == "POST":
        n = request.POST.get('name')
        e = request.POST.get('email')
        p = request.POST.get('pas')
        obj = registerDB(Name=n,Email=e,Password=p)
        obj.save()
        messages.success(request, "Registration successful..!")
        return redirect(user_reg_page)

def Login_user(request):
    if request.method == "POST":
        un = request.POST.get('uname')
        pwd = request.POST.get('pass')
        em = request.POST.get('email')
        if registerDB.objects.filter(Name=un, Password=pwd).exists():
            request.session['Name']=un
            request.session['Password']=pwd
            request.session['Email']=em
            title = "Login Alert!!!"
            ans = "Employee has Logged in to To-Do Site."
            e = 'liyavivek3@gmail.com'
            send_mail(
                title,
                ans,
                'settings.EMAIL_HOST_USER',
                [e],
                fail_silently=False
            )
            title = "Login Successful !"
            ans = "Your have successfully logged in to To-Do Website. Please complete your tasks before due date!"
            send_mail(
                title,
                ans,
                'settings.EMAIL_HOST_USER',
                [em],
                fail_silently=False
            )
            messages.success(request, "Welcome to TO-DO-LIST..!")
            return redirect(User_Home_Page)
        else:
            messages.error(request, "Invalid Username or Password..!")
            return redirect(user_login_page)
    messages.error(request, "Invalid Username or Password..!")
    return redirect(user_login_page)

def UserLogout(request):
    del request.session['Name']
    del request.session['Password']
    messages.warning(request, "Logged out..!")
    return redirect(User_Home_Page)

def my_tasks(request,my_name):
    mydata = taskDB.objects.filter(Employee=my_name)
    return render(request,"my_tasks.html",{'mydata':mydata})

def do_now(request,title):
    title_data=taskDB.objects.get(Task_Title=title)
    return render(request,"donow.html",{'title_data':title_data})

def save_submissions(request):
    if request.method == "POST":
        t = request.POST.get('task')
        e = request.POST.get('emp')
        a = request.POST.get('ans')
        if submissionDB.objects.filter(Task=t).exists():
            return render(request,"already_submitted.html")
        else:
            obj = submissionDB(Task=t, Employee=e, Entry=a)
            obj.save()
            messages.success(request, "Task Submitted Successfully..!")
            return redirect(User_Home_Page)

def task_report_page(request,title2):
    if reportDB.objects.filter(Task_Title=title2).exists():
        title = reportDB.objects.get(Task_Title=title2)
        return render(request,"task_report.html",{'title':title})
    elif submissionDB.objects.filter(Task=title2).exists():
        head = submissionDB.objects.get(Task=title2)
        return render(request,"not_reported.html",{'head':head})
    else:
        return render(request, "yet_to_submit.html")
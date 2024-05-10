from django.urls import path
from frontend import views

urlpatterns = [
    path('User_Home_Page/',views.User_Home_Page,name="User_Home_Page"),
    path('All_Tasks_users/',views.All_Tasks_users,name="All_Tasks_users"),
    path('',views.user_login_page,name="user_login_page"),
    path('user_reg_page/',views.user_reg_page,name="user_reg_page"),
    path('save_reg/',views.save_reg,name="save_reg"),
    path('Login_user/',views.Login_user,name="Login_user"),
    path('UserLogout/',views.UserLogout,name="UserLogout"),
    path('my_tasks/<my_name>',views.my_tasks,name="my_tasks"),
    path('do_now/<title>',views.do_now,name="do_now"),
    path('save_submissions/',views.save_submissions,name="save_submissions"),
    path('task_report_page/<title2>',views.task_report_page,name="task_report_page"),


]
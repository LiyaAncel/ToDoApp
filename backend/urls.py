from django.urls import path
from backend import views

urlpatterns=[
    path('Home_page/',views.Home_page, name='Home_page'),
    path('display_tasks/',views.display_tasks, name='display_tasks'),
    path('save_task/',views.save_task, name='save_task'),
    path('delete_task/<int:tid>',views.delete_task, name='delete_task'),
    path('edit_task/<int:tid>',views.edit_task, name='edit_task'),
    path('update_task/<int:tid>',views.update_task, name='update_task'),
    path('',views.login_page, name='login_page'),
    path('Admin_login_fn/',views.Admin_login_fn, name='Admin_login_fn'),
    path('AdminLogout_fn/',views.AdminLogout_fn, name='AdminLogout_fn'),
    path('task_submissions/',views.task_submissions, name='task_submissions'),
    path('delete_submissions/<title>',views.delete_submissions, name='delete_submissions'),
    path('task_verification/<title>',views.task_verification, name='task_verification'),
    path('save_report/',views.save_report, name='save_report'),
]
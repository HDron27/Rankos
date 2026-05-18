from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('hello/', views.hello, name='hello'),
    path('students/', views.student_list, name='student_list'),
    path('students/add/', views.add_student, name='add_student'),
    path('students/<int:pk>/', views.student_detail, name='student_detail'),
    path('students/<int:pk>/edit/', views.edit_student, name='edit_student'),
    path('students/<int:pk>/delete/', views.delete_student, name='delete_student'),
    path('groups/', views.group_list, name='group_list'),
    path('clubs/', views.club_list, name='club_list'),
    path('profile/edit/', views.profile_edit, name='profile_edit'),
    path('profile/captcha/', views.get_captcha, name='get_captcha'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='students/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]

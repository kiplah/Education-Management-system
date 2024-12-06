from django.urls import path
from . import views
from .views import login_view, logout_view, export_students_csv

urlpatterns = [
    
    path('register/', views.register_student, name='register_student'),
    path('enroll/', views.enroll_student, name='enroll_student'),
    path('payment/', views.make_payment, name='make_payment'),
    path('students/', views.students_list, name='students_list'),
    path('enrollments/', views.enrollments_list, name='enrollments_list'),
    path('payments/', views.payments_list, name='payments_list'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('export/students/', export_students_csv, name='export_students_csv'),
]

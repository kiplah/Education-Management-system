from django.shortcuts import render, redirect
from .forms import StudentForm, EnrollmentForm, PaymentForm
from .models import Student, Enrollment, Payment
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
import csv
from django.http import HttpResponse

from django.shortcuts import render
from .models import Student  # Import your Student model


def home(request):
    return render(request, 'school/home.html')  # Create 'home.html' template

def register_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('students_list')
    else:
        form = StudentForm()
    return render(request, 'school/register_student.html', {'form': form})


def enroll_student(request):
    if request.method == 'POST':
        form = EnrollmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('enrollments_list')
    else:
        form = EnrollmentForm()
    return render(request, 'school/enroll_student.html', {'form': form})


def make_payment(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('payments_list')
    else:
        form = PaymentForm()
    return render(request, 'school/make_payment.html', {'form': form})


def students_list(request):
    query = request.GET.get('q')
    if query:
        students = Student.objects.filter(name__icontains=query)
    else:
        students = Student.objects.all()
    return render(request, 'school/students_list.html', {'students': students})


def enrollments_list(request):
    enrollments = Enrollment.objects.all()
    return render(request, 'school/enrollments_list.html', {'enrollments': enrollments})


def payments_list(request):
    payments = Payment.objects.all()
    return render(request, 'school/payments_list.html', {'payments': payments})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('students_list')
        else:
            return render(request, 'school/login.html', {'error': 'Invalid credentials'})
    return render(request, 'school/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def students_list(request):
    students = Student.objects.all()
    return render(request, 'school/students_list.html', {'students': students})
def export_students_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="students.csv"'
    writer = csv.writer(response)
    writer.writerow(['Name', 'Email', 'Phone', 'Address', 'Student ID'])
    students = Student.objects.all()
    for student in students:
        writer.writerow([student.name, student.email, student.phone, student.address, student.student_id])
    return response
from django import forms
from .models import Student, Enrollment, Payment

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'email', 'phone', 'address', 'student_id']


class EnrollmentForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        fields = ['student', 'course_name', 'date_of_enrollment', 'description']


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['student', 'amount_due', 'amount_paid', 'payment_status', 'payment_date']

from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    student_id = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name


class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course_name = models.CharField(max_length=100)
    date_of_enrollment = models.DateField()
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.student.name} - {self.course_name}"


class Payment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    amount_due = models.DecimalField(max_digits=10, decimal_places=2)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    payment_status = models.CharField(
        max_length=20,
        choices=[('Paid', 'Paid'), ('Pending', 'Pending')],
        default='Pending'
    )
    payment_date = models.DateField()

    def __str__(self):
        return f"{self.student.name} - {self.payment_status}"

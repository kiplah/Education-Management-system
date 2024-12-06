from django.contrib import admin
from .models import Student, Enrollment, Payment

admin.site.register(Student)
admin.site.register(Enrollment)
admin.site.register(Payment)

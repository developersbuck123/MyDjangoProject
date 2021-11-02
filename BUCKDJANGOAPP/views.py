from django.shortcuts import render, redirect
from django.http import HttpResponse
from BUCKDJANGOAPP.models import Student
from BUCKDJANGOAPP.forms import StudentForm


# Create your views here.
def hi(request):
    return HttpResponse('<h1>This is my Home Page</h1>')


def index(request):
    return render(request, './BUCKDJANGOAPP/Index.html')


def student_list(request):
    students = Student.objects.all()
    return render(request, 'BUCKDJANGOAPP/student_list.html', {'students': students})


def create_student(request):
    form = StudentForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('student_list')

    return render(request, 'BUCKDJANGOAPP/students_create.html', {'form': form})


def update_student(request, id):
    students = Student.objects.get(id=id)
    form = StudentForm(request.POST or None, instance=students)

    if form.is_valid():
        form.save()
        return redirect('student_list')

    return render(request, 'BUCKDJANGOAPP/student_update.html', {'students': students, 'form': form})


def delete_student(request, id):
    students = Student.objects.get(id=id)

    if request.method == 'POST':
        students.delete()
        return redirect('student_list')

    return render(request, 'BUCKDJANGOAPP/student_delete.html', {'students': students})

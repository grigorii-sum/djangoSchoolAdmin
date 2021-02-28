from django.shortcuts import render, redirect

from .forms import CreateStudyGroupForm, CreateStudentForm
from .models import StudyGroup, Student


# function for render main page (page with list of study groups)
def school_page(request):
    study_groups = StudyGroup.objects.all()
    context = {
        'title': 'Школа',
        'study_groups': study_groups,
    }
    return render(request, 'main/school_page.html', context)


# function for render page for creating study group
def create_group_page(request):
    if request.method == "POST":
        form = CreateStudyGroupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('school')
    else:
        form = CreateStudyGroupForm()
    context = {
        'title': 'Добавление учебной группы',
        'form': form,
    }
    return render(request, 'main/create_group_page.html', context)


# function for render page with list of student of selected study group
def group_page(request, id):
    students = Student.objects.filter(study_group_id=id).order_by('surname')
    context = {
        'title': 'Учебная группа',
        'students': students,
        'group_id': id,
    }
    return render(request, 'main/group_page.html', context)


# function for render page for creating student
def create_student_page(request, id):
    if request.method == "POST":
        form = CreateStudentForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            student.study_group_id = StudyGroup.objects.get(id=id)
            student.save()
            return redirect('group', id=id)
    else:
        form = CreateStudentForm()
    context = {
        'title': 'Добавление ученика',
        'form': form,
    }
    return render(request, 'main/create_student_page.html', context)

from django.forms import ModelForm, TextInput, Textarea

from .models import StudyGroup, Student


# form for creating StudyGroup
class CreateStudyGroupForm(ModelForm):

    class Meta:
        model = StudyGroup
        fields = ["name"]
        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ввведите название учебной группы'
            }),
        }


# form for creating Student
class CreateStudentForm(ModelForm):

    class Meta:
        model = Student
        fields = ["surname", "name", "patronymic"]
        widgets = {
            "surname": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ввведите фамилию ученика'
            }),
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ввведите имя ученика'
            }),
            "patronymic": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ввведите отчество ученика'
            }),
        }

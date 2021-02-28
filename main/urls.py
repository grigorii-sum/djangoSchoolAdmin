from django.urls import path
from . import views

urlpatterns = [
    path('', views.school_page, name='school'),

    path('create-group', views.create_group_page, name='createGroup'),
    path('group/<int:id>', views.group_page, name='group'),

    path('create-student/<int:id>', views.create_student_page, name='createStudent'),
]

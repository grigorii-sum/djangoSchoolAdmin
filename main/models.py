from django.db import models


class StudyGroup(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Класс'
        verbose_name_plural = 'Классы'


class Student(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    patronymic = models.CharField(max_length=50)
    study_group_id = models.ForeignKey(StudyGroup, on_delete=models.CASCADE)

    def __str__(self):
        return self.surname + " " + self.name + " " + self.patronymic

    class Meta:
        verbose_name = 'Ученик'
        verbose_name_plural = 'Ученики'


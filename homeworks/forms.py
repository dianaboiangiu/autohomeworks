from django import forms
from homeworks.models import Course, Material


class CreatedByFormMixin:

    def save(self, created_by='', commit=True):
        if created_by:
            self.instance.created_by = created_by
        return super().save(commit)


class CourseForm(CreatedByFormMixin, forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'description']


class MaterialForm(forms.ModelForm):
    file = forms.FileField()

    class Meta:
        model = Material
        fields = ['file']

    def save(self, course, commit=True):
        self.instance.course = course
        return super().save(commit)

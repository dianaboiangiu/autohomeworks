from django import forms
from homeworks.models import Course


class CreatedByFormMixin:

    def save(self, created_by='', commit=True):
        if created_by:
            self.instance.created_by = created_by
        return super().save(commit)


class CourseForm(CreatedByFormMixin, forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'description']

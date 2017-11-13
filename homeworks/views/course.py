from django.core.urlresolvers import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from homeworks import forms
from homeworks.models import Course
from .base import CreatedByMixin


class CourseList(ListView):
    template_name = 'course/list.html'
    context_object_name = 'courses'
    model = Course


class CourseDetail(DetailView):
    template_name = 'course/detail.html'
    context_object_name = 'course'
    model = Course


class CourseAdd(CreatedByMixin, CreateView):
    template_name = 'course/add.html'
    form_class = forms.CourseForm

    def get_success_url(self):
        return reverse('course:list')


class CourseEdit(UpdateView):
    template_name = 'course/edit.html'
    form_class = forms.CourseForm
    model = Course

    def get_success_url(self):
        course = self.get_object()
        return reverse('course:detail', kwargs={'pk': course.pk})

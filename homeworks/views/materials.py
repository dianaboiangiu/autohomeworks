
from django.core.urlresolvers import reverse
from django.http import HttpResponseBadRequest
from django.shortcuts import get_object_or_404
from django.views.generic.edit import ModelFormMixin
from django.views.generic import (
    CreateView,
    DeleteView,
    ListView,
)
from homeworks import forms
from homeworks.models import Course, Material


class MaterialList(ListView):
    template_name = 'material/list.html'
    context_object_name = 'materials'
    model = Material

    def get_context_data(self):
        self.course = get_object_or_404(Course, pk=self.kwargs['course_pk'])
        context = super(MaterialList, self).get_context_data()
        context.update({
            'course': self.course,
            'materials': context['materials'].filter(course=self.course),
        })
        return context


class MaterialAdd(CreateView):
    template_name = 'material/add.html'
    form_class = forms.MaterialForm

    def get_success_url(self):
        return reverse('material:list', kwargs={'course_pk': self.course.pk})

    def form_valid(self, form):
        course = self.course
        form.save(course)
        return super(ModelFormMixin, self).form_valid(form)

    def post(self, request, *args, **kwargs):
        self.course = get_object_or_404(Course, pk=self.kwargs['course_pk'])
        form = forms.MaterialForm(request.POST, request.FILES)
        if not self.course:
            raise HttpResponseBadRequest
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class MaterialDelete(DeleteView):
    template_name = 'material/delete.html'
    context_object_name = 'material'
    model = Material

    def get_context_data(self, **kwargs):
        self.course = get_object_or_404(Course, pk=self.kwargs['course_pk'])
        context = super(MaterialDelete, self).get_context_data(**kwargs)
        context.update({
            'course': self.course,
        })
        return context

    def get_success_url(self):
        self.course = get_object_or_404(Course, pk=self.kwargs['course_pk'])
        return reverse('material:list', kwargs={'course_pk': self.course.pk})

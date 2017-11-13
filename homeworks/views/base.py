from django.views.generic.edit import ModelFormMixin


class CreatedByMixin:
    def form_valid(self, form):
        self.object = form.save(created_by=self.request.user)
        return super(ModelFormMixin, self).form_valid(form)

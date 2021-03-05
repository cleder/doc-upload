"""Views."""
from django.views.generic import ListView
from django.views.generic.edit import CreateView

from .models import Document


class DocumentList(ListView):
    template_name = "index.html"
    model = Document


class DocumentCreate(CreateView):
    template_name = "create.html"
    model = Document
    fields = ("title", "tags", "file_upload")
    success_url = "/"

    def form_valid(self, form):
        if len(form.cleaned_data["tags"]) > 5:
            form.errors["tags"] = ["provide no more than 5 tags"]
            return self.form_invalid(form)
        return super().form_valid(form)

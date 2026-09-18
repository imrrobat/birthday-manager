from django.shortcuts import render, redirect, get_object_or_404
from .models import Birthday
from datetime import datetime
from .forms import BirthdayForm

from datetime import datetime

from django.views.generic import ListView


class DateConverter:
    regex = r"\d{4}-\d{2}-\d{2}"

    def to_python(self, value):
        return datetime.strptime(value, "%Y-%m-%d").date()

    def to_url(self, value):
        return value.strftime("%Y-%m-%d")


class BirthdayListView(ListView):
    model = Birthday
    template_name = "home.html"
    context_object_name = "all_birthday"

    def get_queryset(self):
        queryset = Birthday.objects.all()

        query = self.request.GET.get("q", "").strip()

        if query:
            queryset = queryset.filter(name__icontains=query)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["form"] = BirthdayForm()
        context["query"] = self.request.GET.get("q", "").strip()

        return context


def add_birthday(request):
    if request.method == "POST":
        form = BirthdayForm(request.POST)
        if form.is_valid():
            form.save()

        return redirect("home")


def delete_birthday(request, id):
    person = get_object_or_404(Birthday, id=id)
    person.delete()
    return redirect("home")






def edit_birthday(request, id):
    person = get_object_or_404(Birthday, id=id)

    if request.method == "POST":
        form = BirthdayForm(request.POST, instance=person)

        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = BirthdayForm(instance=person)

    all_birthday = Birthday.objects.all()

    return render(request, "home.html", {
        "all_birthday": all_birthday,
        "form": form,
        "editing": True,
        "editing_id": id,
    })
from django.views.generic import (
    TemplateView,
    CreateView,
    ListView,
    UpdateView,
    DeleteView,
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .models import BirthDayRecord
from .forms import BirthDayRecordModelForm


# class BirthDayRecordCreateView(LoginRequiredMixin, CreateView):
#     model = BirthDayRecord
#     fields = ["name", "date_of_birth"]


@login_required
def birth_day_records_view(request):
    birth_day_records = BirthDayRecord.objects.filter(user=request.user)
    form = BirthDayRecordModelForm()

    if request.method == "POST":
        form = BirthDayRecordModelForm(request.POST)

        if form.is_valid():
            birth_day_record = form.save(commit=False)
            birth_day_record.user = request.user
            birth_day_record.save()

        return redirect(".")

    else:
        return render(
            request,
            "pages/home.html",
            context={"birth_day_records": birth_day_records, "form": form},
        )

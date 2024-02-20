import logging

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
from django.views.decorators.http import require_http_methods

from .models import BirthDayRecord
from .forms import BirthDayRecordModelForm



@login_required
def list_create_birthday_records_view(request):
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


@login_required
@require_http_methods(["DELETE"])
def delete_birthday_record_view(request, pk:int):
    record = BirthDayRecord.objects.filter(id=pk, user=request.user)
    if record:
        logging.info(f"Deleting BirthDayRecord {pk} for {request.user}")
    else:
        logging.warning(f"User {request.user} is trying to delete a forbidden record")

    record.delete()

    return redirect("home")
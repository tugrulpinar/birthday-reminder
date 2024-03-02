import logging

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods

from .models import BirthDayRecord
from .forms import BirthDayRecordModelForm



def landing_page(request):
    if request.user.is_authenticated:
        return redirect("profile")
    
    return render(request, "pages/landing_page.html")



@login_required
def profile(request):
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
            "pages/profile.html",
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

    return redirect("profile")


@login_required
def delete_account_view(request):
    if request.method == "POST":
        logging.info(f"User {request.user} is deleting their account")
        user = request.user
        user.delete()
        return redirect("landing-page")

    return render(request, "pages/delete_account.html")
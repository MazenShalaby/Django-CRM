from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models.functions import Concat
from django.db.models import Value, Q
import logging

from .models import Record
from .forms import CreateRecordForm, UpdateRecordForm, SignupForm, LoginForm

# Create your views here.


def home(request):
    context = {}
    return render(request, "app/home.html", context)


##############################################################################################################


@login_required(login_url="signin")
def dashboard(request):

    records = Record.objects.select_related("category").prefetch_related("tags")

    context = {"records": records}
    return render(request, "app/dashboard.html", context)


##############################################################################################################


@login_required(login_url="signin")
def record_detail(request, record_id):
    record = get_object_or_404(Record, id=record_id)

    context = {"record": record}
    return render(request, "app/record_detail.html", context)


##############################################################################################################


@login_required(login_url="signin")
def create_record(request):

    if request.method == "POST":
        form = CreateRecordForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("dashboard")
    else:
        form = CreateRecordForm()

    context = {"form": form}
    return render(request, "app/create_record.html", context)


##############################################################################################################


@login_required(login_url="signin")
def update_record(request, record_id):

    record = get_object_or_404(Record, id=record_id)

    if request.method == "POST":
        form = UpdateRecordForm(data=request.POST, instance=record)
        if form.is_valid():
            form.save()
            return redirect("record-detail", record_id=record_id)
    else:
        form = UpdateRecordForm(instance=record)

    context = {"record": record, "form": form}
    return render(request, "app/update_record.html", context)


##############################################################################################################


@login_required(login_url="signin")
def delete_record(request, record_id):
    record = get_object_or_404(Record, id=record_id)
    record.delete()
    return redirect("dashboard")


##############################################################################################################
logger = logging.getLogger(__name__)


@login_required(login_url="signin")
def search(request):

    query = request.GET.get("query")
    results = []

    try:
        if query:
            results = Record.objects.annotate(
                full_name=Concat("first_name", Value(" "), "last_name")
            ).filter(Q(full_name__icontains=query) | Q(phone__icontains=query))

            if results.count() == 1:
                return redirect("record-detail", results.first().id)

    except Exception as e:
        logger.error(f"An error has occured during search {e}")

    context = {"query": query, "results": results}
    return render(request, "app/search_result.html", context)


##############################################################################################################


def signup(request):

    if request.method == "POST":
        form = SignupForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("signin")
    else:
        form = SignupForm()

    context = {"form": form}
    return render(request, "app/signup.html", context)


##############################################################################################################


def signin(request):

    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("dashboard")
    else:
        form = LoginForm()

    context = {"form": form}
    return render(request, "app/signin.html", context)


##############################################################################################################


@login_required(login_url="signin")
def signout(request):
    logout(request)
    return redirect("signin")


##############################################################################################################


def page_404(request, exception):
    return render(request, "app/404.html", status=404)

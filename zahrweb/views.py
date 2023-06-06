from django.shortcuts import render
from .models import (
    InKindDonation,
    CashDonation,
    News,
    Volunteer,
    Events,
    poster,
    Achivment,
    ExistingProjects,
    About,
    number,
)
from audioop import reverse
from datetime import datetime
from django.shortcuts import get_object_or_404
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.views import generic

from django.contrib import admin
from django.contrib.auth.mixins import LoginRequiredMixin


from django.urls import reverse
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    posters = poster.objects.all().order_by("-id")[:5]
    news = News.objects.order_by("-date")[:3]
    number_of_achivments = number.objects.all()
    active_projects = ExistingProjects.objects.order_by("-start_date")[:3]
    events = Events.objects.all()

    context = {
        "poster_image": posters,
        "news": news,
        "number_of_achivments": number_of_achivments,
        "active_projects": active_projects,
        "events": events,
    }

    return render(request, "index.html", context=context)


def detail(request, primary_key):
    news = News.objects.get(pk=primary_key)
    context = {"news": news}
    return render(request, "news_detail.html", context)


def event_detail(request, primary_key):
    events = Events.objects.get(pk=primary_key)
    context = {"event": events}
    return render(request, "event_detail.html", context)


def project_detail(request, primary_key):
    project = ExistingProjects.objects.get(pk=primary_key)
    context = {"projects": project}
    return render(request, "project_detail.html", context)


def about(request):
    abouts = About.objects.all()
    context = {"abouts": abouts}
    return context


def my_table(request):
    data = [
        {
            "project": "مشروع مكاني",
            "supporter": "UNICEF",
            "audience": "-الاطفال السوريين و الاردنيين من عمر ( 0-18 ) - اليافعين ( 18-24 ) - الامهات السوريات و الاردنيات",
            "cost": "110,000 دينار سنويا",
        },
        {
            "project": "مشروع التوعية ( ACF )",
            "supporter": "ACF",
            "audience": "السوريين و الاردنيين من عمر ( 18-45 )",
            "cost": "20,000 دينار سنويا",
        },
        {
            "project": "مشروع ترخيص المشاريع المنزلية الصغيرة ( IRD )",
            "supporter": "UNHCR",
            "audience": "اصحاب المشاريع الصغيرة السوريين و الاردنيين",
            "cost": "38,000 دينار سنويا",
        },
        {
            "project": "مشروع مصنع المخللات",
            "supporter": "USAID",
            "audience": "المجتمع المحلي",
            "cost": "70,000 دينار",
        },
        {
            "project": "مشروع وزارة الشباب",
            "supporter": "البنك الدولي",
            "audience": "الشباب في مراكز الشباب في لوا بني كنانة",
            "cost": "48,000 دينار",
        },
    ]
    context = {"data": data}
    return context


def my_view(request):
    abouts = about(request)
    table = my_table(request)
    context = {}
    context.update(abouts)
    context.update(table)
    return render(request, "about.html", context)


class NewsListView(generic.ListView):
    model = News
    news_list = "news_list"  # your own name for the list as a template variable
    template_name = "index.html"  # The HTML template for this view

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(NewsListView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context["some_data"] = "This is just some data"
        return context


class NewsDetailView(generic.DetailView):
    model = News
    template_name = "zahrweb/news_detail.html"

    def news_detail_view(request, primary_key):
        try:
            news = News.objects.get(pk=primary_key)
        except News.DoesNotExist:
            raise Http404("News does not exist")

        return render(request, context={"news": news})


class EventDetailView(generic.DetailView):
    model = Events
    template_name = "zahrweb/event_detail.html"

    def Event_detail_view(request, primary_key):
        try:
            event = Events.objects.get(pk=primary_key)
        except Events.DoesNotExist:
            raise Http404("News does not exist")

        return render(request, context={"event": event})


from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

from .forms import SignupForm


def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect("index")
    else:
        form = SignupForm()

    return render(request, "signup.html", {"form": form})


from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate


from .forms import InKindDonationForm, CashDonationForm, IdeaForm, VolunteerForm


def in_kind_donation(request):
    if request.method == "POST":
        form = InKindDonationForm(request.POST)
        if form.is_valid():
            form.save()
            # You can add a success message here
            return redirect("index")  # Replace `home` with your desired URL name
    else:
        form = InKindDonationForm()
    return render(request, "in_kind_donation.html", {"form": form})


def Cash_donation(request):
    if request.method == "POST":
        form = CashDonationForm(request.POST)
        if form.is_valid():
            form.save()
            # You can add a success message here
            return redirect("index")  # Replace `home` with your desired URL name
    else:
        form = CashDonationForm()
    return render(request, "cash_donation.html", {"form": form})


def Idea(request):
    if request.method == "POST":
        form = IdeaForm(request.POST)
        if form.is_valid():
            form.save()
            # You can add a success message here
            return redirect("index")  # Replace `home` with your desired URL name
    else:
        form = IdeaForm()
    return render(request, "idea.html", {"form": form})


@login_required
def volunteer_create(request):
    if request.method == "POST":
        form = VolunteerForm(request.POST)
        if form.is_valid():
            volunteer = form.save(commit=False)
            volunteer.username = request.user
            volunteer.save()
            return redirect("volunteer_success")
    else:
        form = VolunteerForm()
    return render(request, "volunteer_form.html", {"form": form})

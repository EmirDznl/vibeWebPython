
from pathlib import Path
from django.conf import settings
import json
from django.shortcuts import render, redirect
from .forms import SurveyForm
from .models import Customer, Survey


def survey_view(request):
    lang = request.GET.get("lang", "tr")
    json_path = Path(settings.BASE_DIR) / "static" / "data" / "references" / "survey_texts.json"

    with open(json_path, "r", encoding="utf-8") as f:
        texts = json.load(f)

    content = texts.get(lang, texts.get("tr", {}))

    if request.method == "POST":
        form = SurveyForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data["customer_code"]
            customer = Customer.objects.get(customer_code=code)

            survey = form.save(commit=False)
            survey.customer = customer
            survey.save()

            return redirect("survey_success")
    else:
        form = SurveyForm()

    return render(request, "survey.html", {"form": form, "content": content, "lang": lang})


def survey_success_view(request):
    lang = request.GET.get("lang", "tr")
    json_path = Path(settings.BASE_DIR) / "static" / "data" / "references" / "thank_texts.json"

    with open(json_path, "r", encoding="utf-8") as f:
        texts = json.load(f)

    content = texts.get(lang, texts.get("tr", {}))
    return render(request, "survey_success.html", {"content": content, "lang": lang})




def approved_surveys_view(request):
    lang = request.GET.get("lang", "tr")
    json_path = Path(settings.BASE_DIR) / "static" / "data" / "references" / "references_texts.json"

    with open(json_path, "r", encoding="utf-8") as f:
        texts = json.load(f)

    content = texts.get(lang, texts.get("tr", {}))

    # Yalnızca onaylanmış yorumlar
    surveys = Survey.objects.filter(approved=True).order_by('-created_at')

    return render(request, "approved_surveys.html", {"content": content, "surveys": surveys, "lang": lang})
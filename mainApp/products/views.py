
from django.shortcuts import render
from pathlib import Path
import json
from django.conf import settings

def small(request):
    lang = request.GET.get("lang", "tr")
    json_path = Path(settings.BASE_DIR) / "static" / "data" / "products" / "micro_texts.json"

    with open(json_path, "r", encoding="utf-8") as f:
        texts = json.load(f)

    content = texts.get(lang, texts.get("tr", {}))
    return render(request, "smallOrgranisations.html", {"content": content, "lang": lang})




def middle(request):
    lang = request.GET.get("lang", "tr")
    json_path = Path(settings.BASE_DIR) / "static" / "data" / "products" / "orta_texts.json"

    with open(json_path, "r", encoding="utf-8") as f:
        texts = json.load(f)

    content = texts.get(lang, texts.get("tr", {}))
    return render(request, "middleSizeOrganisations.html", {"content": content, "lang": lang})

def enterprise(request):
    lang = request.GET.get("lang", "tr")  # ?lang=en veya ?lang=tr
    json_path = Path(settings.BASE_DIR) / "static" / "data" / "products" / "enterprise_texts.json"

    with open(json_path, "r", encoding="utf-8") as f:
        texts = json.load(f)

    content = texts.get(lang, texts.get("tr", {}))
    return render(request, "enterprise.html", {"content": content, "lang": lang})



from django.shortcuts import render
from pathlib import Path
from django.conf import settings
import json

def erp_management(request):
    lang = request.GET.get("lang", "tr")
    json_path = Path(settings.BASE_DIR) / "static" / "data" / "projMana" / "erp_texts.json"

    with open(json_path, "r", encoding="utf-8") as f:
        texts = json.load(f)

    content = texts.get(lang, texts.get("tr", {}))
    return render(request, "erpManagement.html", {"content": content, "lang": lang})


def integration_management(request):
    lang = request.GET.get("lang", "tr")
    json_path = Path(settings.BASE_DIR) / "static" / "data" / "projMana" / "integration_texts.json"

    with open(json_path, "r", encoding="utf-8") as f:
        texts = json.load(f)

    content = texts.get(lang, texts.get("tr", {}))
    return render(request, "integrationManagement.html", {"content": content, "lang": lang})


def sw_management(request):
    lang = request.GET.get("lang", "tr")
    json_path = Path(settings.BASE_DIR) / "static" / "data" / "projMana" / "sw_texts.json"

    with open(json_path, "r", encoding="utf-8") as f:
        texts = json.load(f)

    content = texts.get(lang, texts.get("tr", {}))
    return render(request, "swManagement.html", {"content": content, "lang": lang})
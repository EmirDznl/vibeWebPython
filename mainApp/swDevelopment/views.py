from django.shortcuts import render
from django.conf import settings
from pathlib import Path
import json

def desktopAppDev(request):
    lang = request.GET.get("lang", "tr")
    json_path = Path(settings.BASE_DIR) / "static" / "data" / "swDev" / "desktop_texts.json"

    with open(json_path, "r", encoding="utf-8") as f:
        texts = json.load(f)

    content = texts.get(lang, texts.get("tr", {}))
    return render(request, "desktopApp.html", {"content": content, "lang": lang})


def webAppDev(request):
    lang = request.GET.get("lang", "tr")
    json_path = Path(settings.BASE_DIR) / "static" / "data" / "swDev" / "web_texts.json"

    with open(json_path, "r", encoding="utf-8") as f:
        texts = json.load(f)

    content = texts.get(lang, texts.get("tr", {}))
    return render(request, "webApp.html", {"content": content, "lang": lang})


def mobileAppDev(request):
    lang = request.GET.get("lang", "tr")  
    json_path = Path(settings.BASE_DIR) / "static" / "data" / "swDev" /"mobile_texts.json"

    with open(json_path, "r", encoding="utf-8") as f:
        texts = json.load(f)

    content = texts.get(lang, texts.get("tr", {}))
    return render(request, "mobileSw.html", {"content": content, "lang": lang})


def apiDevelopment(request):
    lang = request.GET.get("lang", "tr")
    json_path = Path(settings.BASE_DIR) / "static" / "data" / "swDev" /"service_texts.json"

    with open(json_path, "r", encoding="utf-8") as f:
        texts = json.load(f)

    content = texts.get(lang, texts.get("tr", {}))
    return render(request, "serviceDev.html", {"content": content, "lang": lang})

from django.shortcuts import render
from django.conf import settings
from pathlib import Path
import json

def onSiteSupport(request):
    lang = request.GET.get("lang", "tr")
    json_path = Path(settings.BASE_DIR) / "static" / "data" / "supportServices" / "onsite_texts.json"

    with open(json_path, "r", encoding="utf-8") as f:
        texts = json.load(f)

    content = texts.get(lang, texts.get("tr", {}))
    return render(request, "onSiteSupport.html", {"content": content, "lang": lang})

def remoteSupport(request):
    lang = request.GET.get("lang", "tr")
    json_path = Path(settings.BASE_DIR) / "static" / "data" / "supportServices" / "remote_texts.json"

    with open(json_path, "r", encoding="utf-8") as f:
        texts = json.load(f)

    content = texts.get(lang, texts.get("tr", {}))
    return render(request, "remoteSupport.html", {"content": content, "lang": lang})
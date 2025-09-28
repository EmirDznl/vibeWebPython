from django.shortcuts import render
from django.conf import settings
from pathlib import Path
import json

def cloud(request):
    lang = request.GET.get("lang", "tr")
    json_path = Path(settings.BASE_DIR) / "static" / "data" / "serverAndData" / "cloud_texts.json"

    with open(json_path, "r", encoding="utf-8") as f:
        texts = json.load(f)

    content = texts.get(lang, texts.get("tr", {}))
    return render(request, "cloud.html", {"content": content, "lang": lang})


def databaseMaintenance(request):
    lang = request.GET.get("lang", "tr")
    json_path = Path(settings.BASE_DIR) / "static" / "data" / "serverAndData" / "database.json"

    with open(json_path, "r", encoding="utf-8") as f:
        texts = json.load(f)

    content = texts.get(lang, texts.get("tr", {}))
    return render(request, "databaseMaintenance.html", {"content": content, "lang": lang})





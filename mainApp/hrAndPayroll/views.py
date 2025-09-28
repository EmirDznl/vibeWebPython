
from django.shortcuts import render
from pathlib import Path
from django.conf import settings
import json

def hr_view(request):
    lang = request.GET.get("lang", "tr")  # varsayılan dil Türkçe
    json_path = Path(settings.BASE_DIR) / "static" / "data" / "hrAP" / "ik_texts.json"

    with open(json_path, "r", encoding="utf-8") as f:
        texts = json.load(f)

    content = texts.get(lang, texts.get("tr", {}))
    return render(request, "hrManagement.html", {"content": content, "lang": lang})



def payroll_view(request):
    lang = request.GET.get("lang", "tr")  # ?lang=en veya ?lang=tr
    json_path = Path(settings.BASE_DIR) / "static" / "data" / "hrAP" / "payroll.json"

    with open(json_path, "r", encoding="utf-8") as f:
        texts = json.load(f)

    content = texts.get(lang, texts.get("tr", {}))
    return render(request, "payroll.html", {"content": content, "lang": lang})

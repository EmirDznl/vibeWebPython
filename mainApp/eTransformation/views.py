from pathlib import Path
from django.conf import settings
from django.shortcuts import render
from django.urls import include, path
from django.shortcuts import render
from pathlib import Path
from django.conf import settings
import json

def crm(request):
    lang = request.GET.get("lang", "tr")
    json_path = Path(settings.BASE_DIR) / "static" / "data" / "eTrans" / "crm_texts.json"

    with open(json_path, "r", encoding="utf-8") as f:
        texts = json.load(f)

    content = texts.get(lang, texts.get("tr", {}))
    return render(request, "crm.html", {"content": content, "lang": lang})




def eAgreement(request):
    # URL parametresinden dil seçimi (default: 'tr')
    lang = request.GET.get("lang", "tr")
    json_path = Path(settings.BASE_DIR) / "static" / "data" / "eTrans" / "eAggr.json"

    # JSON dosyasını oku
    with open(json_path, "r", encoding="utf-8") as f:
        texts = json.load(f)

    # Seçilen dil veya default Türkçe
    content = texts.get(lang, texts.get("tr", {}))
    return render(request, "eAgreement.html", {"content": content, "lang": lang})

def eBill(request):
    lang = request.GET.get("lang", "tr")
    json_path = Path(settings.BASE_DIR) / "static" / "data" / "eTrans"/"eBill.json"

    with open(json_path, "r", encoding="utf-8") as f:
        texts = json.load(f)

    content = texts.get(lang, texts.get("tr", {}))
    return render(request, "eBill.html", {"content": content, "lang": lang})


def eBook(request):
    lang = request.GET.get("lang", "tr")
    json_path = Path(settings.BASE_DIR) / "static" / "data" / "eTrans" / "eBook.json"

    with open(json_path, "r", encoding="utf-8") as f:
        texts = json.load(f)

    content = texts.get(lang, texts.get("tr", {}))
    return render(request, "eBook.html", {"content": content, "lang": lang})

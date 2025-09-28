from django.shortcuts import render
from django.conf import settings
import json
from pathlib import Path

def budget_management(request):
    # Dil parametresi
    lang = request.GET.get("lang", "tr")

    # JSON dosya yolu
    json_path = Path(settings.BASE_DIR) / "static" / "data" / "businesAnaly" / "budget_texts.json"

    # JSON verisini oku
    with open(json_path, "r", encoding="utf-8") as f:
        texts = json.load(f)

    # Seçilen dil yoksa Türkçe varsayılan
    content = texts.get(lang, texts.get("tr", {}))

    context = {
        "lang": lang,
        "content": content
    }

    return render(request, "budgetManagement.html", context)


def data_report(request):
    lang = request.GET.get("lang", "tr")
    json_path = Path(settings.BASE_DIR) / "static" / "data" / "businesAnaly" / "bi_texts.json"

    with open(json_path, "r", encoding="utf-8") as f:
        texts = json.load(f)

    content = texts.get(lang, texts.get("tr", {}))

    context = {
        "lang": lang,
        "content": content
    }

    return render(request, "dataReport.html", context)

def live_dashboard(request):
    return render(request, 'liveDashboard.html')

from django.shortcuts import render
from django.conf import settings
import json
from pathlib import Path

def digiTransf(request):
    # Dil parametresi, ?lang=en veya ?lang=tr
    lang = request.GET.get("lang", "tr")

    # JSON dosya yolu
    json_path = Path(settings.BASE_DIR) / "static" / "data" / "consulting" / "digiTransf_texts.json"

    # JSON verisini oku
    with open(json_path, "r", encoding="utf-8") as f:
        texts = json.load(f)

    # Seçilen dil yoksa Türkçe varsayılan
    content = texts.get(lang, texts.get("tr", {}))

    return render(request, "digiTransf.html", {"content": content})


def requirementsAnalysis(request):
    # Dil parametresi
    lang = request.GET.get("lang", "tr")

    # JSON dosya yolu
    json_path = Path(settings.BASE_DIR) / "static" / "data" / "consulting" / "reqAnaly_texts.json"

    # JSON verisini oku
    with open(json_path, "r", encoding="utf-8") as f:
        texts = json.load(f)

    # Seçilen dil yoksa Türkçe varsayılan
    content = texts.get(lang, texts.get("tr", {}))

    context = {
        "lang": lang,
        "content": content
    }

    return render(request, "requirementsAnalysis.html", context)


def swTraining(request):
    lang = request.GET.get("lang", "tr")
    json_path = Path(settings.BASE_DIR) / "static" / "data" / "consulting" / "swTraining_texts.json"
    
    with open(json_path, "r", encoding="utf-8") as f:
        texts = json.load(f)
    
    content = texts.get(lang, texts.get("tr", {}))
    
    return render(request, "swTraining.html", {"content": content, "lang": lang})



def workflowConsulting(request):
    # GET parametresinden dil al, yoksa "tr" kullan
    lang = request.GET.get("lang", "tr")
    
    # JSON dosya yolu
    json_path = Path(settings.BASE_DIR) / "static" / "data" / "consulting" / "workflow_texts.json"
    
    # JSON dosyasını aç ve yükle
    with open(json_path, "r", encoding="utf-8") as f:
        texts = json.load(f)
    
    # İstenen dili al, yoksa Türkçe varsayılan
    content = texts.get(lang, texts.get("tr", {}))
    
    # Template'e gönder
    return render(request, "workflowConsulting.html", {"content": content, "lang": lang})
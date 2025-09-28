import json
from django.conf import settings
from django.shortcuts import render

def about(request):
    lang = request.GET.get("lang", "tr")
    json_path = settings.BASE_DIR / "static" / "data" / "about" / "about_texts.json"

    with open(json_path, "r", encoding="utf-8") as f:
        texts = json.load(f)
    

    data = texts.get(lang, texts["tr"])
    return render(request, "about.html", {"texts": data, "lang": lang})

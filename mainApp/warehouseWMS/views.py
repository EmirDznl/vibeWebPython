from django.shortcuts import render

import json
from pathlib import Path
from django.conf import settings
from django.shortcuts import render

def middleWareHouse(request):
    lang = request.GET.get("lang", "tr")
    json_path = Path(settings.BASE_DIR) / "static" / "data" / "warehouseWMS" / "warehouse_texts.json"

    with open(json_path, "r", encoding="utf-8") as f:
        texts = json.load(f)

    content = texts.get(lang, texts.get("tr", {}))
    return render(request, "middleOrganisations.html", {"content": content, "lang": lang})


def smallWareHouse(request):
    lang = request.GET.get("lang", "tr")
    json_path = Path(settings.BASE_DIR) / "static" / "data" /"warehouseWMS"/ "wms_small.json"

    with open(json_path, "r", encoding="utf-8") as f:
        texts = json.load(f)

    content = texts.get(lang, texts.get("tr", {}))
    return render(request, "smallOrganisations.html", {"content": content, "lang": lang})
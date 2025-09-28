from django.shortcuts import render
from django.conf import settings
from pathlib import Path
import json

def workflow_view(request):
    lang = request.GET.get("lang", "tr")
    json_path = Path(settings.BASE_DIR) / "static" / "data" / "workflow" / "workflow_texts.json"

    with open(json_path, "r", encoding="utf-8") as f:
        texts = json.load(f)

    content = texts.get(lang, texts.get("tr", {}))
    return render(request, "workflow.html", {"content": content, "lang": lang})

import json
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib import messages

def edit_json(request):
    json_path = settings.BASE_DIR / "static" / "data" / "core" / "home_texts.json"

    # Dosyayı oku
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        json_string = json.dumps(data, ensure_ascii=False, indent=2)
        
    return render(request, "jsonEditor.html", {"data": json_string})


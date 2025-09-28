from pathlib import Path
from django.shortcuts import render
import json
import os
from django.conf import settings

def home(request):
    # URL parametresi veya session üzerinden dil seçimi yapılabilir, default 'tr'
    lang = request.GET.get('lang', 'tr')
    json_path = Path(settings.BASE_DIR) / "static" / "data" / "core" / "home_texts.json"
    
    with open(json_path, 'r', encoding='utf-8') as f:
        content = json.load(f)
    
    page_content = content.get(lang, content['tr'])  # default TR
    
    return render(request, 'home.html', {'content': page_content})

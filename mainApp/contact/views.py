from .forms import ContactForm
from django.shortcuts import render, redirect
from django.conf import settings
import json
from pathlib import Path




def contact_view_burasi_çalisiyor_daha_sonra_bakılacak_eğer_alttaki_form_göndermezse(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect("contact_success_view")
    else:
        form = ContactForm()

    return render(request, "contact.html", {"form": form})

def contact_view(request):
    lang = request.GET.get("lang", "tr")
    json_path = Path(settings.BASE_DIR) / "static" / "data" / "contact" / "contact_texts.json"

    with open(json_path, "r", encoding="utf-8") as f:
        texts = json.load(f)

    content = texts.get(lang, texts.get("tr", {}))
    return render(request, "contact.html", {"content": content, "lang": lang})


def contact_success_view(request):
    lang = request.GET.get("lang", "tr")
    json_path = Path(settings.BASE_DIR) / "static" / "data" / "contact" / "thankyou_texts.json"

    with open(json_path, "r", encoding="utf-8") as f:
        texts = json.load(f)

    content = texts.get(lang, texts.get("tr", {}))
    return render(request, "contact_success.html", {"content": content})
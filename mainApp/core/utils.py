from django.utils import translation

def get_lang_value(obj):
    """
    obj: { "tr": "Türkçe", "en": "English" }
    Aktif dil veya default "en" döner
    """
    if obj is None:
        return ""
    lang = translation.get_language() or "en"
    return obj.get(lang, obj.get("en", ""))

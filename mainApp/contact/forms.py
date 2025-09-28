from django import forms
from .models import ContactInformation

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactInformation
        fields = ["first_name", "last_name", "email", "phone_number", "message"]
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Tüm alanlara 'form-control' sınıfını ekle
        for field_name, field in self.fields.items():
            # Checkbox gibi özel tipler (KVKK onayı gibi) hariç
            if field.widget.__class__.__name__ not in ['CheckboxInput', 'ClearableFileInput']:
                field.widget.attrs.update({
                    'class': 'form-control',
                    'placeholder': field.label, # Kullanıcıya kolaylık sağlar
                })
            
            # Mesaj alanına özel satır ayarı
            if field_name == 'message':
                 field.widget.attrs['rows'] = 4
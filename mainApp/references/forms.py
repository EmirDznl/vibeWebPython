from django import forms
from .models import Survey, Customer

class SurveyForm(forms.ModelForm):
    customer_code = forms.CharField(max_length=20, label="kodunuz")

    class Meta:
        model = Survey
        fields = ["customer_code", "comment"]

    def clean_customer_code(self):
        code = self.cleaned_data["customer_code"]
        try:
            customer = Customer.objects.get(customer_code=code)
        except Customer.DoesNotExist:
            raise forms.ValidationError("Invalid customer code.")
        return code

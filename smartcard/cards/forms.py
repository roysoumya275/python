from django import forms
from .models import SmartCard

class SmartCardForm(forms.ModelForm):

    name = forms.CharField(
        required=True,
        min_length=3,
        max_length=50
    )

    card_number = forms.CharField(
        required=True,
        min_length=6,
        max_length=12
    )

    balance = forms.DecimalField(
        required=True,
        min_value=0
    )

    class Meta:
        model = SmartCard
        fields = ['name', 'card_number', 'balance']

    # NAME validation
    def clean_name(self):
        name = self.cleaned_data['name']

        if not name.replace(" ", "").isalpha():
            raise forms.ValidationError("Name must contain only letters.")

        return name

    # CARD NUMBER validation
    def clean_card_number(self):
        card_number = self.cleaned_data['card_number']

        if not card_number.isdigit():
            raise forms.ValidationError("Card number must contain digits only.")

        return card_number
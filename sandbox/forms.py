from django import forms
from sandbox.models import Feedback

CHOISES=[('satisfied', 'Satisfied'), ('neutral', 'Neutral'), ('dissatisfied', 'Dissatisfied')]

class FeedbackForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    comment = forms.CharField(widget=forms.Textarea)
    satisfaction = forms.ChoiceField(choices=CHOISES, widget=forms.RadioSelect, required=True)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if '@i.ua' not in email:
            raise forms.ValidationError("Email must be from i.ua domain.")
        return email

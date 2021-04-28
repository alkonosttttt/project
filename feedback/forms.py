from django import forms
from .models import Feedback


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ("fio", "city", "phone", "email", "gender", "service", "notice", "text")

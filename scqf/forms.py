from django.forms import ModelForm, Textarea, TextInput, IntegerField, ChoiceField, RadioSelect
from .models import Feedback

GRADE_CHOICES = [
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),
]

class FeedbackModelForm(ModelForm):
    class Meta:
        model = Feedback
        fields = ['author', 'text', 'grade']

        grade = ChoiceField(widget=RadioSelect, choices = GRADE_CHOICES, required=True)

        widgets = {
            'author': TextInput(attrs={'id': 'input_username', 'placeholder': 'nickname'}),
            'text': Textarea(attrs={'id': 'message', 'placeholder': 'Leave your feedback here..'}),
        }

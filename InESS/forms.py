from django import forms
from .models import Ticket

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'description', 'priority', 'department', 'location']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }

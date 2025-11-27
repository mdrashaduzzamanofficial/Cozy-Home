from django import forms
from .models import Message
from users.models import CustomUser

class MessageForm(forms.ModelForm):
    receiver = forms.ModelChoiceField(queryset=CustomUser.objects.all())

    class Meta:
        model = Message
        fields = ['receiver', 'content']
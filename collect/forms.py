from datetime import date
from django import forms
from .models import Party, Loop, Person


class LoopForm(forms.ModelForm):
    class Meta:
        model = Loop
        exclude = [
            "author",
        ]
        widgets = {
            "course": forms.HiddenInput(),
        }

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["date"].initial = date.today()
        self.fields["date"].widget.attrs.update({"type": "date"})
        self.fields["group"].queryset = Party.objects.filter(author=user).order_by(
            "-id"
        )[:5]
        for field in self.fields.values():
            if field.help_text:
                field.widget.attrs["placeholder"] = field.help_text


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = "__all__"
        widgets = {
            "first_name": forms.TextInput(attrs={"placeholder": "player's name"}),
            "lat": forms.HiddenInput(),
            "lon": forms.HiddenInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            if field.help_text:
                field.widget.attrs["placeholder"] = field.help_text

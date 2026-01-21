from django import forms
from .models import Course, Group, Loop, Person

class LoopForm(forms.ModelForm):
    class Meta:
        model = Loop
        exclude = ["author",]

class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = "__all__"

class PersonForm(forms.ModelForm):

    class Meta:
        model = Person
        fields = "__all__"
        widgets = {
                "first_name": forms.TextInput(attrs={"placeholder": "player's name"}),
                }

    # def save(self, commit=True):
    #     instance = super().save(commit=False)
    #     print(f"{dir(instance)=}")
    #     import pdb
    #     pdb.set_trace()
    #     if not instance.group:
    #         group = Group.objects.create(name=instance.first_name,
    #                              author=self.request.user)
    #     instance.group = group
    #     if commit:
    #         instance.save()
    #     return instance   

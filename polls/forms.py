from django import forms

from polls.models import TeachersM, GroupM


class Teachers(forms.ModelForm):
    class Meta:
        model = TeachersM
        fields = ["name", "surname", "lastname", "birthday", "theme"]


class Group(forms.ModelForm):
    class Meta:
        model = GroupM
        fields = ["name"]

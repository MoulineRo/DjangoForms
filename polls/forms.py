from django import forms


class Teachers(forms.Form):
    name = forms.CharField(label="name", max_length=100)
    surname = forms.CharField(label="surname", max_length=100)
    lastname = forms.CharField(label="last name", max_length=100)
    # birthday = forms.IntegerField(label="birthday")
    birthday1 = forms.IntegerField(label="day", min_value=1, max_value=31)
    birthday2 = forms.IntegerField(label="month", min_value=1, max_value=12)
    birthday3 = forms.IntegerField(label="year", min_value=1950, max_value=2023)
    theme = forms.CharField(label="theme", max_length=100)


class Group(forms.Form):
    name = forms.CharField(label="name", max_length=100)

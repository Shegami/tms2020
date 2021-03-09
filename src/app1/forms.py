from django.forms import Form, CharField, IntegerField


class UserForm(Form):
    age = IntegerField(
        min_value=1,
        max_value=99
    )
    first_name = CharField(max_length=15)

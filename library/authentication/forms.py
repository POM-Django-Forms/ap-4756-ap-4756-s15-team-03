from django import forms


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"


class RegisterForm(LoginForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    middle_name = forms.CharField(required=False)
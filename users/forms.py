from django import forms
from django.contrib.auth.forms import UserCreationForm
from . import models


class LoginForm(forms.Form):

    email = forms.EmailField(widget=forms.EmailInput(
        attrs={"placeholder": "Email"}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Password"})
    )

    def clean(self):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        try:
            user = models.User.objects.get(email=email)
            if user.check_password(password):
                return self.cleaned_data
            else:
                self.add_error(
                    "password", forms.ValidationError("Password is wrong"))
        except models.User.DoesNotExist:
            self.add_error("email", forms.ValidationError(
                "User does not exist"))


class SignUpForm(forms.ModelForm):
    """Form definition for SignUp."""

    class Meta:
        """Meta definition for SignUpform."""

        model = models.User
        fields = ('email', 'name', 'birthdate')
        widgets = {
            'email': forms.EmailInput(attrs={"placeholder": "이메일 주소를 입력하세요"}),
            'name': forms.TextInput(attrs={"placeholder": "이름을 입력하세요"}),
            'birthdate': forms.DateTimeInput()
        }

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "비밀번호 입력"})
    )

    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "비밀번호 확인"})
    )

    def clean_password1(self):
        password = self.cleaned_data.get("password")
        password1 = self.cleaned_data.get("password1")

        if password != password1:
            raise forms.ValidationError("비밀번호를 확인해주세요.")
        else:
            return password

    def save(self, *args, **kwrgs):
        user = super().save(commit=False)
        email = self.cleaned_data.get("email")
        password = self.clean_password1()
        name = self.cleaned_data.get("name")
        # name = self.get("name")
        user.name = name
        user.username = email
        user.set_password(password)
        user.save()

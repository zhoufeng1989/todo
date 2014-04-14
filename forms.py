from django import forms
from todo.models import User, Item
from django.contrib.auth import authenticate


class RegisterForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput,
                                min_length=12)
    password2 = forms.CharField(label='Password confirmation',
                                widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('name', 'email', 'mobile')

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and (password1 != password2):
            raise forms.ValidationError('password do not match')
        return password2

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']
        user = authenticate(username=email, password=password)
        if not user:
            raise forms.ValidationError('email or password not correct')
        return self.cleaned_data


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('content', 'priority', 'finish_time')

    def save(self, commit=True):
        item = super(ItemForm, self).save(commit=False)
        if commit:
            item.save()
        return item

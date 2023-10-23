# from django import forms

# from .models import ConsumerUser, ConsumerLogin


# class ConsumerUserForm(forms.ModelForm):
#     class Meta:
#         model = ConsumerUser
#         fields = ['username','email', 'password1', 'password2']
#         widgets = {
#             'password1': forms.PasswordInput(),
#             'password2': forms.PasswordInput(),
#         }

#     def clean(self):
#         cleaned_data = super().clean()

#         # Ensure that password1 and password2 match
#         password1 = cleaned_data.get('password1')
#         password2 = cleaned_data.get('password2')
#         if password1 != password2:
#             raise forms.ValidationError('The passwords do not match')

#         return cleaned_data

# class ConsumerLoginForm(forms.ModelForm):
#     class Meta:
#         model = ConsumerLogin
#         fields = ['email', 'password']
#         widgets = {
#             'password': forms.PasswordInput(),
#         }

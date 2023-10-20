from django import forms

from contact_module.models import ContactUs


class ContactUsForm(forms.Form):
    full_name = forms.CharField(
        label='',
        max_length=50,
        error_messages={
            'required': 'لطفا نام و نام خانوادگی خود را وارد کنید',
            'max_length': 'نام و نام خانوادگی نمیتواند بیشتر از 50 کاراکتر باشد',
        },
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'نام و نام خانوادگی',
            }
        )
    )
    email = forms.EmailField(
        label='',
        widget=forms.EmailInput(

            attrs={
                'class': 'form-control',
                'placeholder': 'ایمیل',
            }
        ))
    title = forms.CharField(
        label='',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'عنوان',
            }
        ))
    message = forms.CharField(
        label='',
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': 'متن پیام',
                'id': 'message'
            }
        ))


class ContactUsModelForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ['full_name', 'email', 'title', 'message']
        widgets= {
            'full_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'email': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'message': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': '5',
                    'id': 'message'
                }
            ),
        }
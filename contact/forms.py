from django import forms
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox
  
  
class ContactForm(forms.Form):
    email = forms.EmailField()
    feedback = forms.CharField(widget=forms.Textarea)
    # captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)
    captcha = ReCaptchaField(
    public_key='6Lcnh60nAAAAAE1kaGgQtzrDgZFMu5NROdso8yYM',
    private_key='6Lcnh60nAAAAAHSyCX7leVh8TPq_u5Wtp2RspX6W',
)
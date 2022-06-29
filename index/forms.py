from django import forms
from index.models import UserInfo
class TitleSearch(forms.Form):
    title=forms.CharField(label='书名',label_suffix='',error_messages={'required':'请输入正确的title'})

class UserModelForm(forms.ModelForm):
    class Meta:
        model=UserInfo
        fields="__all__"
        widgets={"password":forms.TextInput}
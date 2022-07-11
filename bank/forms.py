from django import forms
from bank.models import Reclog
class stform(forms.ModelForm):
    class Meta:
        model=Reclog
        fields=['Recname', 'Recno', 'Amt','Curr']

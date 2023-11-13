from django import forms

from staff.models import Employer, Position


class EmployerForm(forms.ModelForm):

    class Meta:
        model = Employer
        fields = (
            'name',
            'surname',
            'patronymic',
            'date_contract',
            'position',
        )


class PositionForm(forms.ModelForm):
    class Meta:
        model = Position
        fields = ('title',)

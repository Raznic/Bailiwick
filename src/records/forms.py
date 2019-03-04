from django.forms import ModelForm, TextInput, ModelChoiceField, Select
from domains.models import Domain
from . import models


class ARecordForm(ModelForm):

    class Meta:
        model = models.ARecord
        exclude = ["id"]
        widgets = {
            "hostname": TextInput(
                attrs={
                    "class": "validate",
                }
            )
        }

    domain = ModelChoiceField(
        queryset=Domain.objects.all(),
        empty_label=None,
        widget=Select(
            attrs={
                "class": "browser-default",
            }
        )
    )

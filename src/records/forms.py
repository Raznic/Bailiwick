from django.forms import ModelForm, TextInput, ModelChoiceField, Select
from domains.models import Domain
from . import models


class RecordForm(ModelForm):

    domain = ModelChoiceField(
        queryset=Domain.objects.all(),
        empty_label=None,
        widget=Select(
            attrs={
                "class": "browser-default",
            }
        )
    )


class ARecordForm(RecordForm):

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


class NsRecordForm(RecordForm):

    class Meta:
        model = models.NsRecord
        exclude = ["id"]
        widgets = {
            "name_server": TextInput(
                attrs={
                    "class": "validate",
                }
            ),
            "owner": TextInput(
                attrs={
                    "class": "validate",
                }
            ),
        }

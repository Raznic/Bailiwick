from django.forms import ModelForm, TextInput, ModelChoiceField, Select
from registries.models import Registry
from . import models


class DomainForm(ModelForm):

    class Meta:
        model = models.Domain
        exclude = ["id"]
        widgets = {
            "name": TextInput(
                attrs={
                    "class": "validate",
                }
            )
        }

    registry = ModelChoiceField(
        queryset=Registry.objects.all(),
        empty_label=None,
        widget=Select(
            attrs={
                "class": "browser-default",
            }
        )
    )

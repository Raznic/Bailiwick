from django.forms import ModelForm, TextInput
from . import models


class RegistryForm(ModelForm):

    class Meta:
        model = models.Registry
        exclude = ["id"]
        widgets = {
            "name": TextInput(
                attrs={
                    "class": "validate",
                }
            )
        }

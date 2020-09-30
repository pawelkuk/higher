from django import forms
from . import models
from django.core.exceptions import ValidationError


class AddMarkForm(forms.ModelForm):
    class Meta:
        model = models.Grade
        fields = ["candidate", "recruiter", "task", "value"]

    def clean(self):
        cleaned_data = super().clean()
        candidate = cleaned_data.get("candidate")
        recruiter = cleaned_data.get("recruiter")
        task = cleaned_data.get("task")

        already_graded = models.Grade.objects.all().filter(
            task__exact=task, recruiter__exact=recruiter, candidate__exact=candidate
        )
        if already_graded:
            # Only do something if both fields are valid so far.
            raise ValidationError(
                (
                    "The task has been already graded. "
                    "A recruiter can't grade a candidate on the same task multiple times."
                )
            )

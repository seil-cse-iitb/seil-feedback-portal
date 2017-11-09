from django.db import models


# Create your models here.

class Question(models.Model):
    TEXT = 'text'
    SINGLE_CHOICE = 'single'
    MULTI_CHOICE = 'multi'
    answer_type_choices = (
        (None, "Choose a type for answers!"),
        (
            "Answer Type", [
                (TEXT, 'Text'),
                (SINGLE_CHOICE, 'Single choice'),
                (MULTI_CHOICE, 'Multi choice'),
            ]
        ),
    )
    # Fields
    id = models.AutoField
    text = models.CharField(max_length=500,help_text="This field is the question that will be shown")
    answer_type = models.CharField(max_length=10, choices=answer_type_choices)
    created_on = models.DateTimeField(auto_now_add=True,editable=False)
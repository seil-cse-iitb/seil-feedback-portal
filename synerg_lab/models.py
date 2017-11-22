from django.db import models


class CommonModel(models.Model):
    id = models.AutoField
    created_on = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        abstract = True


class Room(CommonModel):
    name = models.CharField(max_length=100,
                            help_text="What is the room generally called? ex:- seil lab,circular hall etc")
    short_name = models.CharField(max_length=50, help_text="Short name of the room. ex:- SIC 201,SIA 310 etc")

    def __str__(self):
        return "%s the room aka %s" % (self.name, self.short_name)


class Region(CommonModel):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, help_text="This will be displayed to users while giving feedback.")
    description = models.CharField(max_length=50, blank=True, help_text="Describe the region if required")

    def __str__(self):
        return "%s the region in %s" % (self.name, self.room)


class Sensor(CommonModel):
    HUMIDITY = 'H'
    TEMPERATURE = 'T'
    HUMIDITY_TEMPERATURE = 'H_T'
    sensor_type_choices = ((None, "Choose sensor type!"),
                           (HUMIDITY, "Humidity"),
                           (TEMPERATURE, "Temperature"),
                           (HUMIDITY_TEMPERATURE, "Humidity and Temperature"),
                           )
    sensor_type = models.CharField(max_length=50, choices=sensor_type_choices)
    region = models.ManyToManyField(Region)

    def __str__(self):
        return "%s the sensor in %s" % (self.id, self.region)


class User(CommonModel):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, help_text="Full name of user")
    username = models.CharField(max_length=50, help_text="username for login", primary_key=True)
    password = models.CharField(max_length=50, help_text="password for login")
    email = models.EmailField(max_length=100, help_text="Email for contacting the user")
    height = models.FloatField(help_text="Meta data for future study(if available)", blank=True, null=True)
    weight = models.FloatField(help_text="Meta data for future study(if available)", blank=True, null=True)

    def __str__(self):
        return "%s the user with username %s and email %s at room %s" % (
            self.name, self.username, self.email, self.room)


class Question(CommonModel):
    region = models.ManyToManyField(Region)
    question_text = models.CharField(max_length=500, help_text="This will be shown as question for feedback")
    SINGLE = 'S'
    MULTIPLE = 'M'
    answer_type_choices = ((None, "Choose answer type!"),
                           (SINGLE, "Single Choice Answer"),
                           (MULTIPLE, "Multiple Choice Answer"),
                           )
    answer_type = models.CharField(max_length=50, choices=answer_type_choices,
                                   help_text="Single Choice Answer will render radio button for answers while Multiple"
                                             " Choice Answer will render check box for answers")

    def __str__(self):
        return "%s the question(%s) with question text %s" % (self.id, self.answer_type, self.question_text)


class Answer(CommonModel):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=200, help_text="This will be shown as a answer of related question")
    user = models.ManyToManyField(User, through='UserAnswer')

    def __str__(self):
        return "%s the answer of %s" % (self.answer_text, self.question)


class UserAnswer(CommonModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    answer_time = models.DateTimeField()

    def __str__(self):
        return "user %s at time %s gives answer %s" % (self.user, self.answer_time, self.answer)


# Create your models here.
class QuestionDemo(models.Model):
    SINGLE_CHOICE = 'single'
    MULTI_CHOICE = 'multi'
    answer_type_choices = (
        (None, "Choose a type for answers!"),
        (
            "Answer Type", [
                (SINGLE_CHOICE, 'Single choice'),
                (MULTI_CHOICE, 'Multi choice'),
            ]
        ),
    )
    # Fields
    id = models.AutoField
    text = models.CharField(max_length=500, help_text="This field is the question that will be shown")
    answer_type = models.CharField(max_length=10, choices=answer_type_choices)
    created_on = models.DateTimeField(auto_now_add=True, editable=False)

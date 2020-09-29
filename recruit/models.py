from django.db import models
import uuid


class Recruiter(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Candidate(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Task(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100, null=False)

    def __str__(self):
        return f"{self.title}"


class Grade(models.Model):
    """Grading on the scale described in the Dreyfus model."""

    class GradeChoices(models.IntegerChoices):
        NOVICE = (1, "Novice")
        ADV_BEGINNER = (2, "Advanced beginner")
        COMPETENT = (3, "Competent")
        PROFICIENT = (4, "Proficient")
        EXPERT = (5, "Expert")

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    value = models.IntegerField(choices=GradeChoices.choices)
    recruiter = models.ForeignKey(Recruiter, on_delete=models.CASCADE)
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.candidate} graded with {self.value} by {self.recruiter} on {self.task}"

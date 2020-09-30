from .forms import AddMarkForm
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.db.models import Avg
from . import models


class AddMarkView(FormView):
    template_name = "recruit/addmarkform.html"
    form_class = AddMarkForm
    success_url = reverse_lazy("api:add_mark")

    def form_valid(self, form):
        candidate = models.Candidate.objects.get(id=form.data["candidate"])
        recruiter = models.Recruiter.objects.get(id=form.data["recruiter"])
        task = models.Task.objects.get(id=form.data["task"])
        grade = models.Grade(
            value=form.data["value"],
            candidate=candidate,
            recruiter=recruiter,
            task=task,
        )
        grade.save()
        return super().form_valid(form)


def candidates(request):
    all_grades = models.Grade.objects.all()

    average_grade_per_candidate = all_grades.values("candidate").annotate(Avg("value"))
    data = []
    for c in average_grade_per_candidate:

        candidate = {}
        candidate["id"] = c["candidate"]
        candidate["full_name"] = str(models.Candidate.objects.get(id=c["candidate"]))
        candidate["avg_grade"] = round(c["value__avg"], 2)
        candidate["grades"] = [
            g.value for g in all_grades.filter(candidate__id=c["candidate"])
        ]
        data.append(candidate)
    return JsonResponse({"data": data})

from django.contrib import admin
from . import models

admin.site.register([models.Recruiter, models.Candidate, models.Task, models.Grade])

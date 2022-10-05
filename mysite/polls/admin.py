from django.contrib import admin

from .models import Choice, Question

# make the polls app modifiable
admin.site.register(Choice)
admin.site.register(Question)
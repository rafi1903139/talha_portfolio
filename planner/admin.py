from django.contrib import admin
from .models import AreaOfExpertise, Education, Experience, ExpertiseItem, LanguageSkill, OrganizationalAffiliation, Participation, Portfolio, Reference, SoftwareName, SoftwareSkill, Training, ExtraCurricular, TrainingSection, TrainingSubSection 

# Register your models here.

admin.site.register(Participation)
admin.site.register(Experience)
admin.site.register(OrganizationalAffiliation)
admin.site.register(Education)
admin.site.register(TrainingSection)
admin.site.register(TrainingSubSection)
admin.site.register(Training)
admin.site.register(Portfolio)
admin.site.register(ExtraCurricular)
admin.site.register(AreaOfExpertise)
admin.site.register(ExpertiseItem)
admin.site.register(SoftwareSkill)
admin.site.register(SoftwareName)
admin.site.register(LanguageSkill)
admin.site.register(Reference)





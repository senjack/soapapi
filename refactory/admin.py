from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Administrator,Staff,Applicant,RefactoryUser
from .models import Cohort
from .models import Catalyst
from .models import Bootcamp
from .models import Contact
from .models import EducationBackground
from .models import SkillSet
from .models import Honor
from .models import ApplicationVideo
from .models import Interview
from .models import Role
from .models import AdministratorRole

# Register your models here.

admin.site.register(RefactoryUser)

admin.site.register(Administrator)

admin.site.register(Staff)

admin.site.register(Applicant)


admin.site.register(Cohort) 
admin.site.register(Catalyst)
admin.site.register(Bootcamp)
admin.site.register(Contact)
admin.site.register(EducationBackground)
admin.site.register(SkillSet)
admin.site.register(Honor)
admin.site.register(ApplicationVideo)
admin.site.register(Interview)
admin.site.register(Role)
admin.site.register(AdministratorRole)

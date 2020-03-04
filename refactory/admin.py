from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Administrator, Staff, Applicant, RefactoryUser
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
from .models import InterviewCategory, StructureIndicator, CategoryStructure, InterviewSet, InterviewSelection, Room, Batch

refactory_models_list = [InterviewCategory,
                         RefactoryUser, Administrator, Staff, Applicant, Cohort, Catalyst, Bootcamp, Contact, EducationBackground, SkillSet, Honor, ApplicationVideo, Interview, Role, AdministratorRole, StructureIndicator, CategoryStructure, InterviewSet, InterviewSelection, Room, Batch]
admin.site.register(refactory_models_list)

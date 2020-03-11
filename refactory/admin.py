from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Administrator, Staff, Applicant, RefactoryUser
from .models import Cohort
from .models import Catalyst
from .models import Bootcamp
from .models import Contact
from .models import EducationBackground
from .models import SkillSet
from .models import ApplicationVideo
from .models import Interview
from .models import Role
from .models import AdministratorRole
from .models import InterviewCategory, StructureIndicator, CategoryStructure, InterviewSet, InterviewSelection, Room, Batch, Partner, Application, Competence, Admission,CatalystApplication,BootcampApplication,AdvertisementSubChannelSet,ApplicantChannelSelection,AdvertisementChannelSet

refactory_models_list = [InterviewCategory,
                         RefactoryUser, Administrator, Staff, Applicant, Cohort, Catalyst, Bootcamp, Contact, EducationBackground, SkillSet, ApplicationVideo, Interview, Role, AdministratorRole, StructureIndicator, CategoryStructure, InterviewSet, InterviewSelection, Room, Batch, Partner, Application, Competence, Admission,CatalystApplication,BootcampApplication,AdvertisementSubChannelSet,ApplicantChannelSelection,AdvertisementChannelSet]
admin.site.register(refactory_models_list)

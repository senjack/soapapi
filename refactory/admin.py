from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import * 

refactory_models_list = [
    RefactoryUser, 
    Administrator, 
    Partner,
    Staff, 
    Applicant,
    Role,
    AdministratorRole,
    PartnerRole,
    StaffRole,    
    Accessibility,
    AdministratorAccessibility,
    PartnerAccessibility,
    StaffAccessibility,
    ApplicantAccessibility,
    Cohort,
    Catalyst,
    Bootcamp,
    Contact,
    EducationBackground,
    SkillSet,
    Skill,
    Project,
    Certificate,
    Referee,
    AdvertisementChannelSet,
    AdvertisementSubChannelSet,
    ApplicantChannelSelection,
    Application,
    CatalystApplication,
    BootcampApplication,
    Competence,
    ApplicationVideo,
    Room,
    Batch,
    InterviewSet,
    InterviewSelection,
    InterviewSchedule,
    CategoryStructure,
    StructureIndicator,
    Interview,
    InterviewScore,
    Admission
]

admin.site.register(refactory_models_list)

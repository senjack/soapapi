from django.urls import path,include
from rest_framework.urlpatterns import format_suffix_patterns
from refactory import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'cohort', views.CohortViewSet)

router1 = routers.DefaultRouter()
router1.register(r'catalyst', views.CatalystViewSet)

router2 = routers.DefaultRouter()
router2.register(r'bootcamp', views.BootcampViewSet)

router3 = routers.DefaultRouter()
router3.register(r'contact', views.ContactViewSet)

router4 = routers.DefaultRouter()
router4.register(r'EducationBackground', views.EducationBackgroundViewSet)

router5 = routers.DefaultRouter()
router5.register(r'SkillSet', views.SkillSetViewSet)

router6 = routers.DefaultRouter()
router6.register(r'honor', views.HonorViewSet)

router7 = routers.DefaultRouter()
router7.register(r'ApplicationVideo', views.ApplicationVideoViewSet)

router8 = routers.DefaultRouter()
router8.register(r'Interview', views.InterviewViewSet)
urlpatterns = [
    
    
]

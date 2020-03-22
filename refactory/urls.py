from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from refactory import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register('cohorts', views.CohortViewSet)
router.register('catalysts', views.CatalystViewSet)
router.register('bootcamps', views.BootcampViewSet)
router.register('contacts', views.ContactViewSet)
router.register('education-backgrounds', views.EducationBackgroundViewSet)
router.register('skill-sets', views.SkillSetViewSet)
router.register('application-videos', views.ApplicationVideoViewSet)
router.register('interviews', views.InterviewViewSet)
router.register('Projects', views.ProjectView)


urlpatterns = [
    path('', include(router.urls)),
]

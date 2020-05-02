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
router.register('projects', views.ProjectView)
router.register('certificates', views.CertificateView)
router.register('referees', views.RefereeView)
router.register('advertisement-channelsets', views.AdvertisementChannelSetView)
router.register('advertisement-subchannels', views.AdvertisementSubChannelSetView)
router.register('applications', views.ApplicationView)
router.register('catalyst-applications', views.CatalystApplicationView)
router.register('bootcamp-appliactions', views.BootcampApplicationView)
router.register('competencies', views.CompetenceView)
router.register('rooms', views.RoomView)
router.register('batches', views.BatchView)
router.register('Projects', views.InterviewCategoryView)
router.register('structure-indicators', views.InterviewSetView)
router.register('panelists', views.InterviewScheduleView)
router.register('partners', views.CategoryStructureView)
router.register('structure-indicators', views.StructureIndicatorView)
router.register('partners', views.PartnerView)
router.register('admissions', views.AdmissionView)


urlpatterns = [
    path('', include(router.urls)),
]

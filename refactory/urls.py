from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from refactory import views
from rest_framework import routers
from django.conf.urls import url, include


router = routers.DefaultRouter()
router.register(r'^', views.CohortViewSet)

router1 = routers.DefaultRouter()
router1.register(r'catalyst', views.CatalystViewSet)

router2 = routers.DefaultRouter()
router2.register(r'bootcamp', views.BootcampViewSet)

router3 = routers.DefaultRouter()
router3.register(r'contact', views.ContactViewSet)

router4 = routers.DefaultRouter()
router4.register(r'education-background', views.EducationBackgroundViewSet)

router5 = routers.DefaultRouter()
router5.register(r'skill-set', views.SkillSetViewSet)

router6 = routers.DefaultRouter()
router6.register(r'honor', views.HonorViewSet)

router7 = routers.DefaultRouter()
router7.register(r'application-video', views.ApplicationVideoViewSet)

router8 = routers.DefaultRouter()
router8.register(r'Interview', views.InterviewViewSet)

urlpatterns = [

    url(r'^cohort/', include(router.urls)),
    url(r'^catalyst/', include(router1.urls)),
    url(r'^contact/', include(router2.urls)),
    url(r'^cohort/', include(router3.urls)),
    url(r'^education-background/', include(router4.urls)),
    url(r'^skill-set/', include(router5.urls)),
    url(r'^honor/', include(router6.urls)),
    url(r'^Application-video/', include(router7.urls)),
    url(r'^Interview/', include(router8.urls)),
]

"""soapapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path


from django.conf.urls import url, include
from refactory.models import RefactoryUser
from rest_framework import routers, serializers, viewsets
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RefactoryUser
        fields = ['url',  'email', 'password']

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            if attr == 'password':
                instance.set_password(value)
            else:
                setattr(instance, attr, value)
        instance.save()
        return instance

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = RefactoryUser.objects.all()
    serializer_class = UserSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
#    url(r'^api-auth/', include('rest_framework.urls'))

    url(r'^users/', include(router.urls)),
   
   # Default
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # jwt
    path(r'api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path(r'api/token/refresh/',TokenRefreshView.as_view(), name='token_refresh'),

    # login
    path(r'rest-auth/', include('rest_auth.urls')),

    path(r'rest-auth/registration/', include('rest_auth.registration.urls')),


    url(r'^apis', include('refactory.urls')),

]

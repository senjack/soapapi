from rest_framework import serializers

from .models import Cohort
from .models import Catalyst
from .models import Bootcamp
from .models import Contact
from .models import EducationBackground
from .models import SkillSet
# from .models import Honor
from .models import ApplicationVideo
from .models import Interview


class CohortSerializer (serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cohort
        fields = ('cohort_id', 'name_name', 'registration_date', 'start_date',
                  'end_date', 'cohort_number', 'description', 'running')


class CatalystSerializer (serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Catalyst
        fields = ('catalyst_id', 'name_name', 'registration_date', 'start_date',
                  'end_date', 'catalyst_number', 'description', 'running')


class BootcampSerializer (serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Bootcamp
        fields = ('bootcamp_id', 'name_name', 'registration_date', 'start_date',
                  'end_date', 'bootcamp_number', 'description', 'running')


class ContactSerializer (serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Contact
        fields = ('applicant_id', 'linkedin_link',
                  'twitter_link', 'facebook_link')


class EducationBackgroundSerializer (serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EducationBackground
        fields = ('applicant_id', 'school', 'degree', 'Field_of_study',
                  'grade', 'From', 'to', 'Extra_activity')


class SkillSetSerializer (serializers.HyperlinkedModelSerializer):
    class Meta:
        SkillSet
    fields = ('skill_id', 'skill_name', 'description')


# class HonorSerializer (serializers.HyperlinkedModelSerializer):
#     class Meta:
#         Honor
#     fields = ('applicant_id', 'honor_title', 'association',
#               'Issuer', 'date_of_honor', 'Description')


class ApplicationVideoSerializer (serializers.HyperlinkedModelSerializer):
    class Meta:
        ApplicationVideo
    fields = ('application_id', 'videolink')


class InterviewSerializer (serializers.HyperlinkedModelSerializer):
    class Meta:
        Interview
    fields = ('schedule_id', 'interview_id', 'start_date', 'end_date')

from django.db import models

# Create your models here.


class Application(models.Model):
    application_id = models.ForeignKey(
        application_id, on_delete=models.CASCADE)
    catalyst_id = models.ForeignKey(catalyst_id, on_delete=models.CASCADE)
    bootcamp_id = models.ForeignKey(bootcamp_id, on_delete=models.CASCADE)
    startdate = models.CharField(max_length=30)
    enddate = models.CharField(max_length=50)
    complete = models.CharField(max_length=80)
    selected = models.CharField(max_length=100)
    interviewed = models.CharField(max_length=110)
    admitted = models.CharField(max_length=120)


class Competence(models.Model):
    application_id = models.ForeignKey(application, on_delete=models.CASCADE)
    link = models.CharField(max_length=50)
    application_video = models.CharField(max_length=80)
    video_link = models.CharField(max_length=100)


class Interview_category(models.Model):
    category_id = models.IntegerField(primary_key=True)
    category_name = models.CharField(max_length=50)
    category_desciption = models.CharField(max_length=100)


class Category_structure(models.Model):
    structure_id = models.CharField(max_length=80)
    structure_name = models.CharField(max_length=100)
    structure_description = models.CharField(max_length=120)


class structure_indicator(models.Model):
    indictor_id = models.CharField(max_length=80)
    indictor_name = models.CharField(max_length=100)
    indictor_description = models.CharField(max_length=120)


class Interview_set(models.Model):
    set_id = models.CharField(max_length=80)
    set_name = models.CharField(max_length=100)
    category_id = models.ForeignKey(category_id, on_delete=models.CASCADE)
    set_description = models.CharField(max_length=120)
    date_start = models.CharField(max_length=100)
    date_end = models.CharField(max_length=60)


class Interview_selection(models.Model):
    interview_set = models.ForeignKey(interview_set, on_delete=models.CASCADE)
    application_id = models.ForeignKey(
        application_id, on_delete=models.CASCADE)
    selection_id = models.IntegerField(primary_key=True)
    selection_date = models.CharField(max_length=60)


class Room(models.Model):
    room_id = models.IntegerField(primary_key=True)
    rooom_name = models.CharField(max_length=60)
    room_location = models.CharField(max_length=100)
    description = models.CharField(max_length=120)


class Batch(models.Model):
    batch_id = models.IntegerField(primary_key=True)
    batch_name = models.CharField(max_length=80)
    batch_description = models.CharField(max_length=100)
    creation_date = models.CharField(max_length=120)
    room_id = models.ForeignKey(room_id, on_delete=models.CASCADE)

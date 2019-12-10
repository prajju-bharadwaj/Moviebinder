from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    project_image = models.ImageField(null=True, blank=True, upload_to="projects-images/")
    is_completed = models.BooleanField(default=False, null=True)
    company_name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Script(models.Model):
    script_title = models.CharField(max_length=100)
    script_content = models.TextField()
    edited_on = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return self.script_title

class ShotList(models.Model):
    scene_num = models.IntegerField()
    shot_num = models.IntegerField()
    shot_desc = models.CharField(max_length=100)
    shot_type = models.CharField(max_length=50)
    shot_size = models.IntegerField(choices=((1,("Close Up Shot")),(2,("Long Shot")),(3,("Medium Shot"))),default=1)
    movement = models.IntegerField(choices=((1,("Static")),(2,("Pan")),(3,("Tilt")),(4,("Tracking"))),default=1)
    project = models.ForeignKey(Project, on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return self.shot_desc

class Schedule(models.Model):
    scene_no = models.IntegerField()
    scene_type = models.IntegerField(choices=((1,("Interior")),(2,("Exterior")),(3,("Interior/Exterior"))),default=1)
    scene_desc = models.CharField(max_length=100)
    mode = models.IntegerField(choices=((1,("Day")),(2,("Night")),(3,("Morning")),(4,("Afternoon")),(5,("Evening")),(6,("Sunrise")),(7,("Sunset"))),default=1)
    location = models.CharField(max_length=100)
    project = models.ForeignKey(Project, on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return self.scene_desc



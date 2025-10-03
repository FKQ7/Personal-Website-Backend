from django.db import models

class Skill(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"#{self.name}"


class Experience(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    link = models.URLField(blank=True, null=True)
    date = models.CharField(max_length=100, blank=True, null=True)
    skills = models.ManyToManyField(Skill, related_name="Experience", blank=True)


    def __str__(self):
        return self.title


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.URLField(blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    skills = models.ManyToManyField(Skill, related_name="projects", blank=True)

    def __str__(self):
        return self.title
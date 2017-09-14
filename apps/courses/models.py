from __future__ import unicode_literals

from django.db import models

class CourseManager(models.Manager):
    def validate(self, post_data):
        errors = {}
        if len(post_data['html_name']) < 5:
            errors["name"] = "Course name should be more than 5 characters"
        if len(post_data['html_desc']) < 15:
            errors["desc"] = "Course description should be more than 15 characters"
        return errors

class Course(models.Model):
    name = models.CharField(max_length = 255)
    desc = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = CourseManager()

class Comment(models.Model):
    comment = models.CharField(max_length = 255)
    course = models.ForeignKey(Course, related_name = "comments")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

# class Desc(models.Model):
#     desc = models.TextField()
#     course = models.OneToOneField(Course, related_name = "desc")
#     created_at = models.DateTimeField(auto_now_add = True)
#     updated_at = models.DateTimeField(auto_now = True)
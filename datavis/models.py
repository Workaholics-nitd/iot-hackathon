import datetime

from django.db import models


class Dustbin(models.Model):
    dustbin_id = models.CharField(max_length=200)
    percentage = models.IntegerField()
    collect_time = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.dustbin_id


class Comment(models.Model):
    # dustbin = models.ForeignKey(
    #     Dustbin,
    #     on_delete=models.CASCADE,
    # )
    user = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.text

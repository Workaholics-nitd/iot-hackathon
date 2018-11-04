from django.db import models


class StorePercentage(models.Model):
    dustbin_id = models.CharField(max_length=200)
    percentage = models.IntegerField('percentage filled')
    collect_time = models.DateTimeField('time collected')

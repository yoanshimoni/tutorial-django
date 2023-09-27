from djongo import models


class AppVersion(models.Model):
    _id = models.ObjectIdField()
    version = models.CharField(max_length=50, null=False, blank=False)
    date = models.TimeField(auto_now=True)

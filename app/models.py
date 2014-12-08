from django.db import models

class Host(models.Model):
    name = models.CharField(max_length=32)
    address = models.CharField(max_length=45)
    tunnel = models.ForeignKey('Tunnel', blank=True, null=True, on_delete=models.SET_NULL)
    def __str__(self):
        return self.name

class Tunnel(models.Model):
    name = models.CharField(max_length=32)
    address = models.CharField(max_length=45, blank=True, null=True)
    interface = models.CharField(max_length=16)
    status = models.CharField(max_length=16, blank=True, null=True)
    updated = models.PositiveIntegerField(blank=True, null=True)
    metadata = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.name

    

from django.db import models

# Create your models here.

class Note(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    adat = models.CharField(max_length=100, null=True)
    code = models.CharField(max_length=100, null=True)
    name = models.CharField(max_length=100, null=True)
    obs = models.CharField(max_length=200, null=True)
    reba = models.IntegerField()
    rena = models.CharField(max_length=100, null=True)
    stat = models.IntegerField()
    final = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s %s %s %s %s %s %s %s %s %s' % (self.id, self.adat, self.code, self.name, self.obs, self.reba,
                                                  self.rena, self.stat, self.final, self.created_at)


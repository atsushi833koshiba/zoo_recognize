from django.db import models

class ZooCollection(models.Model):
    user_id = models.IntegerField(default=0)
    animal_id= models.IntegerField(default=0)

    def __str__(self):
        return '%d, %d' % (self.user_id, self.animal_id)


class AnimalInfo(models.Model):
    id = models.AutoField(primary_key=True)
    animal_id = models.IntegerField(default=0)
    animal_name = models.CharField(max_length=50,default='')
    animal_title = models.CharField(max_length=300,default='')
    animal_disc = models.TextField(default='')

    def __str__(self):
        return '%d, %s, %s %s' % (self.animal_id, self.animal_name, self.animal_name, self.animal_disc)

class ZooRecognization(models.Model):
    name = models.CharField(max_length=128, null=True, default="unknown")
    animal_id = models.IntegerField(default=0)
    score = models.FloatField("score of the classification", default=0.0, null=True)

from django.db import models

# Create your models here.
class Poll(models.Model):
  title = models.CharField(max_length=100)
  description = models.TextField(blank=True)
  technology = models.CharField(max_length=20)
  created_at = models.DateTimeField(auto_now_add=True)
  
  def __str__(self):
    return '{}'.format(self.title)
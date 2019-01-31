from django.db import models
from django.urls import reverse_lazy

# Create your models here.
class Bookmark(models.Model):
    site_name = models.CharField(max_length=50)
    url = models.URLField()

    def __str__(self):
        return self.site_name+" : "+self.url
    # Todo :get_absolute_url method

    class Meta:
        ordering=['site_name']

    def get_absolute_url(self):
        return reverse_lazy('bookmark_detail', args=[self.id])



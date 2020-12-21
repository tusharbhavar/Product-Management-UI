from django.db import models

class Categories(models.Model):
    name = models.CharField(max_length=200)
    tag = models.CharField(max_length=200, blank=True)
    image = models.ImageField(default = 'pic_folder/None/no-img.jpg')
    category = models.CharField(max_length=200, blank=True)
    description = models.TextField()

    def __str__(self):
        return self.name
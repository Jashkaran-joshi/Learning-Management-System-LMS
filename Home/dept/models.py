from django.db import models

# Create your models here.
from django.db import models
from django.utils.text import slugify

class Dept(models.Model):
    name = models.CharField(max_length=100, unique=True)
    code = models.CharField(max_length=20, unique=True)
    head_of_dept = models.CharField(max_length=100, blank=True)
    
    established_year = models.PositiveIntegerField(blank=True, null=True)
    description = models.TextField(blank=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)
            unique_slug = base_slug
            counter = 1
            while Dept.objects.filter(slug=unique_slug).exists():
                unique_slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = unique_slug
        super(Dept, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} ({self.code})"

from django.db import models
from django.utils.text import slugify

class Subject(models.Model):
    name = models.CharField(max_length=100, unique=True, blank=True)
    code = models.CharField(max_length=20, unique=True, blank=True)
    teacher = models.ForeignKey('teacher.Teacher', on_delete=models.CASCADE, related_name='subjects')
    description = models.TextField(blank=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)
            unique_slug = base_slug
            counter = 1
            while Subject.objects.filter(slug=unique_slug).exists():
                unique_slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = unique_slug
        super(Subject, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} ({self.code})"
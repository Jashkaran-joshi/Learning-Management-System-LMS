from django.db import models
from django.utils.text import slugify

class Teacher(models.Model):
    DEPARTMENT_CHOICES = [
        ('Mathematics', 'Mathematics'),
        ('Physics', 'Physics'),
        ('Chemistry', 'Chemistry'),
        ('Biology', 'Biology'),
        ('History', 'History'),
        ('Geography', 'Geography'),
        ('English', 'English'),
        ('Computer Science', 'Computer Science'),
        ('General', 'General'),
    ]

    name = models.CharField(max_length=100)
    teacher_code = models.CharField(max_length=255, unique=True, blank=True)
    department = models.CharField(max_length=100, choices=DEPARTMENT_CHOICES)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True)
    designation = models.CharField(max_length=100)
    bio = models.TextField(blank=True)
    image = models.ImageField(upload_to='teacher_images/', blank=True, null=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)
            unique_slug = base_slug
            counter = 1
            while Teacher.objects.filter(slug=unique_slug).exists():
                unique_slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = unique_slug
        super(Teacher, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} ({self.teacher_code})"
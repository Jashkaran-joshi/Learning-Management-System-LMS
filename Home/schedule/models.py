from django.db import models
from django.utils.text import slugify

class Exam(models.Model):
    EXAM_TYPE_CHOICES = [
        ('Midterm', 'Midterm'),
        ('Final', 'Final'),
        ('Quiz', 'Quiz'),
        ('Practical', 'Practical'),
        ('Oral', 'Oral'),
        ('Other', 'Other'),
    ]

    SUBJECT_CHOICES = [
        ('Mathematics', 'Mathematics'),
        ('Physics', 'Physics'),
        ('Chemistry', 'Chemistry'),
        ('Biology', 'Biology'),
        ('History', 'History'),
        ('Geography', 'Geography'),
        ('English', 'English'),
        ('Computer Science', 'Computer Science'),
        ('Other', 'Other'),
    ]

    title = models.CharField(max_length=200)
    exam_code = models.CharField(max_length=20, unique=True)
    exam_type = models.CharField(max_length=50, choices=EXAM_TYPE_CHOICES)
    subject = models.CharField(max_length=100, choices=SUBJECT_CHOICES)
    teacher = models.CharField(max_length=100)
    exam_date = models.DateField()
    duration_minutes = models.PositiveIntegerField()
    total_marks = models.PositiveIntegerField()
    passing_marks = models.PositiveIntegerField()
    description = models.TextField(blank=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            unique_slug = base_slug
            counter = 1
            while Exam.objects.filter(slug=unique_slug).exists():
                unique_slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = unique_slug
        super(Exam, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} ({self.exam_code})"
    
class Event(models.Model):
    EVENT_TYPE_CHOICES = [
        ('Seminar', 'Seminar'),
        ('Workshop', 'Workshop'),
        ('Conference', 'Conference'),
        ('Webinar', 'Webinar'),
        ('Social', 'Social'),
        ('Cultural', 'Cultural'),
        ('Sports', 'Sports'),
        ('Other', 'Other'),
    ]

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

    title = models.CharField(max_length=200)
    event_code = models.CharField(max_length=20, unique=True)
    event_type = models.CharField(max_length=50, choices=EVENT_TYPE_CHOICES)
    department = models.CharField(max_length=100, choices=DEPARTMENT_CHOICES)
    organizer = models.CharField(max_length=100)
    event_date = models.DateField()
    start_time = models.TimeField()
    duration_minutes = models.PositiveIntegerField()
    location = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            unique_slug = base_slug
            counter = 1
            while Event.objects.filter(slug=unique_slug).exists():
                unique_slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = unique_slug
        super(Event, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} ({self.event_code})"

class Holiday(models.Model):
    HOLIDAY_TYPE_CHOICES = [
        ('Public', 'Public'),
        ('National', 'National'),
        ('Religious', 'Religious'),
        ('Cultural', 'Cultural'),
        ('Institutional', 'Institutional'),
        ('Other', 'Other'),
    ]

    title = models.CharField(max_length=200)
    holiday_code = models.CharField(max_length=20, unique=True)
    holiday_type = models.CharField(max_length=50, choices=HOLIDAY_TYPE_CHOICES)
    department = models.CharField(
        max_length=100,
        choices=[
            ('All', 'All Departments'),
            ('Mathematics', 'Mathematics'),
            ('Physics', 'Physics'),
            ('Chemistry', 'Chemistry'),
            ('Biology', 'Biology'),
            ('History', 'History'),
            ('Geography', 'Geography'),
            ('English', 'English'),
            ('Computer Science', 'Computer Science'),
        ],
        default='All'
    )
    date = models.DateField()
    description = models.TextField(blank=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            unique_slug = base_slug
            counter = 1
            while Holiday.objects.filter(slug=unique_slug).exists():
                unique_slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = unique_slug
        super(Holiday, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} ({self.holiday_code})"
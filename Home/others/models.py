from django.db import models
from django.utils.text import slugify

class Book(models.Model):
    GENRE_CHOICES = [
    ('Fiction', 'Fiction'),
    ('Non-Fiction', 'Non-Fiction'),
    ('Science', 'Science'),
    ('History', 'History'),
    ('Biography', 'Biography'),
    ('Children', 'Children'),
    ('Other', 'Other'),
    ]
    
    title = models.CharField(max_length=200)
    isbn = models.CharField(max_length=13, unique=True)
    genre = models.CharField(max_length=50, choices=GENRE_CHOICES)
    author = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)
    publish_date = models.DateField()
    number_of_pages = models.PositiveIntegerField()
    number_of_copies = models.PositiveIntegerField(default=1)
    language = models.CharField(max_length=50, default='English')
    description = models.TextField(blank=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            unique_slug = base_slug
            counter = 1
            while Book.objects.filter(slug=unique_slug).exists():
                unique_slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = unique_slug
        super(Book, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} ({self.isbn})"

class Sport(models.Model):
    SPORT_TYPE_CHOICES = [
        ('Team', 'Team'),
        ('Individual', 'Individual'),
        ('Dual', 'Dual'),
        ('Extreme', 'Extreme'),
        ('Other', 'Other'),
    ]

    name = models.CharField(max_length=100, unique=True)
    sport_type = models.CharField(max_length=50, choices=SPORT_TYPE_CHOICES)
    number_of_players = models.PositiveIntegerField(help_text="Number of players per team or individual")
    origin_country = models.CharField(max_length=100)
    equipment_required = models.TextField(blank=True)
    rules = models.TextField(blank=True)
    governing_body = models.CharField(max_length=100, blank=True)
    popularity_rank = models.PositiveIntegerField(null=True, blank=True)
    olympic_sport = models.BooleanField(default=False)
    image = models.ImageField(upload_to='sports/', blank=True)
    description = models.TextField(blank=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)
            unique_slug = base_slug
            counter = 1
            while Sport.objects.filter(slug=unique_slug).exists():
                unique_slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = unique_slug
        super(Sport, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.name}"

class Hostel(models.Model):
    HOSTEL_TYPE_CHOICES = [
        ('Boys', 'Boys'),
        ('Girls', 'Girls'),
        ('Co-ed', 'Co-ed'),
    ]

    name = models.CharField(max_length=200)
    hostel_type = models.CharField(max_length=20, choices=HOSTEL_TYPE_CHOICES)
    location = models.CharField(max_length=255)
    warden_name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15)
    email = models.EmailField(blank=True)
    total_rooms = models.PositiveIntegerField()
    available_rooms = models.PositiveIntegerField()
    facilities = models.TextField(blank=True) 
    rules = models.TextField(blank=True)
    image = models.ImageField(upload_to='hostels/', blank=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)
            unique_slug = base_slug
            counter = 1
            while Hostel.objects.filter(slug=unique_slug).exists():
                unique_slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = unique_slug
        super(Hostel, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} ({self.location})"

class Transport(models.Model):
    TRANSPORT_TYPE_CHOICES = [
        ('Bus', 'Bus'),
        ('Van', 'Van'),
        ('Car', 'Car'),
        ('Auto', 'Auto'),
        ('Other', 'Other'),
    ]

    name = models.CharField(max_length=100)
    transport_type = models.CharField(max_length=20, choices=TRANSPORT_TYPE_CHOICES)
    registration_number = models.CharField(max_length=50, unique=True)
    capacity = models.PositiveIntegerField()
    driver_name = models.CharField(max_length=100)
    driver_contact = models.CharField(max_length=15)
    route_details = models.TextField(blank=True) 
    available_timings = models.CharField(max_length=255, blank=True) 
    associated_hostel = models.ForeignKey('Hostel', on_delete=models.CASCADE, related_name='transports')
    image = models.ImageField(upload_to='transports/', blank=True)

    def __str__(self):
        return f"{self.name} - {self.transport_type} ({self.registration_number})"
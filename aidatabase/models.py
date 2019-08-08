from django.conf import settings
from django.db import models
from django.utils import timezone


class Ai(models.Model):
    CHOOSE3 = (("1", "1"), ("2", "2"), ("3", "3"))
    CHOOSE4 = (("1", "X"), ("2", "XX"), ("3", "XXX"), ("4", "XXXX"))
    CHOOSE5 = (("1", "X"), ("2", "XX"), ("3", "XXX"), ("4", "XXXX"), ("5", "XXXXX"))
    ai_id = models.AutoField(primary_key=True)
    book_id = models.ForeignKey('Book', on_delete=models.PROTECT)
    name = models.CharField(max_length=20, help_text="", verbose_name="")
    gender = models.CharField(choices=CHOOSE5, max_length=1)
    short_name = models.CharField(max_length=10)
    manifestation = models.TextField()
    physical = models.CharField(choices=CHOOSE5, max_length=1)
    difference = models.TextField()
    technical = models.CharField(choices=CHOOSE3, max_length=1)
    consciousness = models.CharField(choices=CHOOSE5, max_length=1)
    intelligence = models.CharField(choices=CHOOSE4, max_length=1)
    free_will = models.BooleanField()
    learning = models.BooleanField()
    emotional = models.BooleanField()
    integration = models.CharField(choices=CHOOSE4, max_length=1)
    on_purpose = models.BooleanField()
    creator_rel = models.CharField(choices=CHOOSE3, max_length=1)
    owner_rel = models.CharField(choices=CHOOSE3, max_length=1)
    female_creator = models.BooleanField()
    society_pos = models.CharField(choices=CHOOSE3, max_length=1)
    subject = models.CharField(choices=CHOOSE3, max_length=1)
    servant = models.CharField(choices=CHOOSE3, max_length=1)
    intimacy = models.CharField(choices=CHOOSE4, max_length=1)
    told_by = models.CharField(choices=CHOOSE3, max_length=1)
    quantity = models.CharField(choices=CHOOSE3, max_length=1)
    warrior = models.BooleanField()
    rebellious = models.BooleanField()
    harmed_humans = models.BooleanField()
    harms_creator = models.BooleanField()
    more_control = models.BooleanField()
    world_domination = models.BooleanField()
    alien_technology = models.BooleanField()
    explicit_mention = models.BooleanField()
    registered_on = models.DateTimeField(blank=True, null=True)
    registered_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)

    def publish(self):
        self.registered_on = timezone.now()
        self.save()

    def __str__(self):
        return self.name

class Book(models.Model):
    book_id = models.AutoField(primary_key=True)
    author_id = models.ForeignKey('Author', on_delete=models.PROTECT)
    title = models.CharField(max_length=30)
    series_id = models.ForeignKey('Series', on_delete=models.PROTECT)
    publish_year = models.IntegerField()
    registered_on = models.DateTimeField(blank=True, null=True)
    registered_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)

    def publish(self):
        self.registered_on = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Series(models.Model):
    author_id = models.ForeignKey('Author', on_delete=models.PROTECT)
    series_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    registered_on = models.DateTimeField(blank=True, null=True)
    registered_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)

    def publish(self):
        self.registered_on = timezone.now()
        self.save()

    def __str__(self):
        return self.name

class Author(models.Model):
    author_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    female = models.BooleanField()
    registered_on = models.DateTimeField(blank=True, null=True)
    registered_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)

    def publish(self):
        self.registered_on = timezone.now()
        self.save()

    def __str__(self):
        return self.name
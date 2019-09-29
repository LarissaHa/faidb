from django.conf import settings
from django.db import models
from django.utils import timezone
# from django.contrib.contenttypes.fields import GenericForeignKey
# from django.contrib.contenttypes.models import ContentType
# from django.contrib.contenttypes.fields import GenericRelation


class Ai(models.Model):
    ai_id = models.AutoField(primary_key=True)
    registered_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    registered_on = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    source_id = models.ForeignKey('Source', on_delete=models.PROTECT, default="")
    # Ich habe oben nicht gesagt, dass AIs einzigartig sind. Ich missbrauche die Klasse 
    # AI mal für Reviews und hole alles über "key_name zusammen". Ich hoffe, das funktioniert.
    name = models.CharField("Real Name", max_length=50)
    short_name = models.CharField("Short Name", max_length=15)

    def publish(self):
        self.registered_on = timezone.now()
        self.save()

    def __str__(self):
        return self.name

class Review(models.Model):
    rev_id = models.AutoField(primary_key=True, default=0)
    CHOOSE3 = (("1", "1"), ("2", "2"), ("3", "3"))
    CHOOSE4 = (("1", "X"), ("2", "XX"), ("3", "XXX"), ("4", "XXXX"))
    CHOOSE5 = (("1", "X"), ("2", "XX"), ("3", "XXX"), ("4", "XXXX"), ("5", "XXXXX"))
    ai_id = models.ForeignKey('Ai', on_delete=models.PROTECT)
    # key_name = models.CharField(max_length=30, help_text="bookname-ainame", verbose_name="")
    gender = models.CharField(choices=CHOOSE5, max_length=1)
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
    registered_on = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    registered_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)

    def publish(self):
        self.registered_on = timezone.now()
        self.save()

    def __str__(self):
        return '{} ({})'.format(
            self.ai_id.name,
            self.rev_id)

class Source(models.Model): 
    NOVEL = 'NL'
    COMIC = 'CO'
    MANGA = 'MG'
    FILM = 'FM'
    SERIES = 'SE'
    ANIME = 'AN'
    GAME = 'GM'
    NOVELLA = 'NA'
    SHORTSTORY = 'SS'
    MAGAZINE = 'MZ'
    OTHER = 'OT'
    MEDIUM_TYPES = ((NOVEL, "novel"), (COMIC, "comic"), (MANGA, "manga"), (FILM, "film"), (SERIES, "series"), (ANIME, "anime"), (GAME, "game"), (NOVELLA, "novella"), (SHORTSTORY, "shortstory"), (MAGAZINE, "magazine"), (OTHER, "other"))
    medium_type = models.CharField(max_length=2, choices=MEDIUM_TYPES)
    source_id = models.AutoField(primary_key=True)
    publish_year = models.IntegerField("first published")
    website = models.URLField(blank=True)
    title = models.CharField(max_length=60)
    registered_on = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    registered_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    creator = models.ManyToManyField("Person", related_name='created', blank=True)

    def publish(self):
        self.registered_on = timezone.now()
        self.save()

    def __str__(self):
        return self.title
"""
class Series(models.Model):
    # author_id = models.ForeignKey('Author', on_delete=models.PROTECT)
    series_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    registered_on = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    registered_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)

    def publish(self):
        self.registered_on = timezone.now()
        self.save()

    def __str__(self):
        return self.name
"""
class Person(models.Model):
    person_id = models.AutoField(primary_key=True)
    # name = models.CharField('lastname-firstname(s)', max_length=30)
    firstname = models.CharField('firstname', default="firstname", max_length=30)
    lastname = models.CharField('lastname', default="lastname", max_length=30)
    female = models.BooleanField()
    website = models.URLField(blank=True)
    registered_on = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    registered_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    add_information = models.TextField("Some Additional Information", blank=True, null=True)

    def publish(self):
        self.registered_on = timezone.now()
        self.save()

    def __str__(self):
        return '{}, {}'.format(
            self.lastname,
            self.firstname)

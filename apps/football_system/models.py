from django.db import models
from django.contrib.auth.models import AbstractUser

class Person(AbstractUser):
    class TypeAdministrator(models.TextChoices):
        TECHNICAL_DIRECTOR = 'TD', 'Director Técnico'
        PLANNER = 'PR', 'Planillero'
        USER = 'CU', 'Usuario'


    type = models.CharField(
        "tipo",
        max_length=2,
        choices=TypeAdministrator.choices,
        default=TypeAdministrator.USER,
    )

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'

class FootballCategory(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Categoría de Futboll'
        verbose_name_plural = 'Categorías de Futboll'

    def __str__(self):
        return self.name


class Club(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Club'
        verbose_name_plural = 'Clubs'

    def __str__(self):
        return self.name
    

class Team(models.Model):
    name = models.CharField("nombre", max_length=100)
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    category = models.ForeignKey(FootballCategory, on_delete=models.CASCADE)
    logo = models.ImageField(upload_to='logos/', blank=True, null=True)

    class Meta:
        verbose_name = 'Equipo'
        verbose_name_plural = 'Equipos'

    def __str__(self):
        return self.name


class Player(models.Model):
    name = models.CharField(max_length=100)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='players/', blank=True, null=True)
    suspended = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Jugador'
        verbose_name_plural = 'Jugadores'

    def __str__(self):
        return self.name


class Match(models.Model):
    local_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='local_matches')
    visiting_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='visiting_matches')
    date = models.DateTimeField()
    category = models.ForeignKey(FootballCategory, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Partido'
        verbose_name_plural = 'Partidos'

    def __str__(self):
        return f"{self.local_team} vs {self.visiting_team}"

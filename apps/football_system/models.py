import cv2, os
import numpy as np
from io import BytesIO
from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.files import File
from django.db import models
from django.contrib.auth.models import AbstractUser


class Club(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Club'
        verbose_name_plural = 'Clubs'

    def __str__(self):
        return self.name
    

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

    profile_picture = models.ImageField(
        "foto de perfil",
        upload_to="profile_pictures/",
        blank=True,
        null=True,
    )

    club = models.ForeignKey(Club, on_delete=models.CASCADE, blank=True, null=True)

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
    

class Match(models.Model):
    category = models.ForeignKey(FootballCategory, on_delete=models.CASCADE)

    local_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='local_matches')
    visiting_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='visiting_matches')

    local_team_image = models.ImageField(upload_to='match_images/', blank=True, null=True)
    visiting_team_image = models.ImageField(upload_to='match_images/', blank=True, null=True)

    recognition_local_team_image = models.ImageField(upload_to='recognition_match_images/', blank=True, null=True)
    recognition_visiting_team_image = models.ImageField(upload_to='recognition_match_images/', blank=True, null=True)


    date = models.DateTimeField()

    class Meta:
        verbose_name = 'Partido'
        verbose_name_plural = 'Partidos'

    def __str__(self):
        return f"{self.local_team} vs {self.visiting_team}"

    def clean(self):
        # Obtener las imágenes de los equipos
        local_team_image = self.local_team_image
        visiting_team_image = self.visiting_team_image

        if local_team_image:
            # Procesar local_team_image y guardar el resultado en recognition_local_team_image
            recognition_local_team_image = self.process_image(local_team_image)
            self.recognition_local_team_image.save(
                'recognition_match_images/processed_{}_local_team.jpg'.format(self.id),  # Cambia el nombre según tu lógica
                File(recognition_local_team_image)
            )

        if visiting_team_image:
            # Procesar visiting_team_image y guardar el resultado en recognition_visiting_team_image
            recognition_visiting_team_image = self.process_image(visiting_team_image)
            self.recognition_visiting_team_image.save(
                'recognition_match_images/processed_{}_visiting_team.jpg'.format(self.id),  # Cambia el nombre según tu lógica
                File(recognition_visiting_team_image)
            )

        return super().clean()
    
    def process_image(self, image):
        # Realizar el procesamiento de la imagen aquí
        # Por ejemplo, usar OpenCV para el reconocimiento facial
        # Debes implementar la lógica adecuada según tus necesidades
        # Devolver la imagen procesada
        processed_image = image  # Esto es un ejemplo, debes reemplazarlo con la lógica real
        return processed_image

class Player(models.Model):
    name = models.CharField(max_length=100)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='players/', blank=True, null=True)

    class Meta:
        verbose_name = 'Jugador'
        verbose_name_plural = 'Jugadores'

    def __str__(self):
        return self.name
    
class PlayerSuspension(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    start_date = models.DateField()
    num_matches = models.PositiveIntegerField()
    reason = models.TextField(blank=True)

    class Meta:
        verbose_name = 'Suspensión de Jugador'
        verbose_name_plural = 'Suspensiones de Jugadores'

    def __str__(self):
        return f"Suspensión de {self.player.name} - {self.num_matches} partidos"

    def end_date(self):
        from datetime import timedelta
        return self.start_date + timedelta(days=self.num_matches * 7)
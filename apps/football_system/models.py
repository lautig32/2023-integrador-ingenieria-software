from django.core.files import File
from django.db import models
from django.contrib.auth.models import AbstractUser

from apps.recognition_system.models import FaceRecognition


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

    # def clean(self):
    #     # Obtener las imágenes de los equipos
    #     local_team_image = self.local_team_image
    #     visiting_team_image = self.visiting_team_image

    #     if local_team_image:
    #         recognition_local_team_image = self.process_image_local_team(local_team_image)

    #         if self.recognition_local_team_image:
    #             self.recognition_local_team_image.delete()

    #         self.recognition_local_team_image.save(
    #             'processed_{}_local_team.jpg'.format(self.id),
    #             File(recognition_local_team_image)
    #         )

    #         recognition_local_team_image.close()
    #         # os.remove(recognition_local_team_image)

    #     if visiting_team_image:
    #         recognition_visiting_team_image = self.process_image_visiting_team(visiting_team_image)

    #         if self.recognition_visiting_team_image:
    #             self.recognition_visiting_team_image.delete()

    #         self.recognition_visiting_team_image.save(
    #             'processed_{}_visiting_team.jpg'.format(self.id),
    #             File(recognition_visiting_team_image)
    #         )

    #         recognition_visiting_team_image.close()

    #     return super().clean()
    
    # def process_image_local_team(self, image):
    #     images_search = []

    #     # List of images to search for faces
    #     qs_search_players = Player.objects.filter(team=self.local_team)

    #     for qs in qs_search_players:
    #         images_search.append(qs.photo.url)

    #     face_recognition = FaceRecognition(images_search)

    #     imagen_objetivo_path = f"{self.local_team_image.url}"

    #     result_image = face_recognition.recognize_faces(imagen_objetivo_path)

    #     processed_image = result_image
    #     return processed_image
    
    # def process_image_visiting_team(self, image):
    #     images_search = []
                
    #     # List of images to search for faces
    #     qs_search_players = Player.objects.filter(team=self.visiting_team)

    #     for qs in qs_search_players:
    #         images_search.append(qs.photo.url)

    #     for qs in qs_search_players:
    #         images_search.append(qs.photo.url)

    #     face_recognition = FaceRecognition(images_search)

    #     imagen_objetivo_path = f"{self.visiting_team_image.url}"

    #     result_image = face_recognition.recognize_faces(imagen_objetivo_path)

    #     processed_image = result_image
    #     return processed_image

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
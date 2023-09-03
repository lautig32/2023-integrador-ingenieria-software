# Generated by Django 4.2.1 on 2023-09-03 23:09

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Club',
                'verbose_name_plural': 'Clubs',
            },
        ),
        migrations.CreateModel(
            name='FootballCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Categoría de Futboll',
                'verbose_name_plural': 'Categorías de Futboll',
            },
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='players/')),
            ],
            options={
                'verbose_name': 'Jugador',
                'verbose_name_plural': 'Jugadores',
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='nombre')),
                ('logo', models.ImageField(blank=True, null=True, upload_to='logos/')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='football_system.footballcategory')),
                ('club', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='football_system.club')),
            ],
            options={
                'verbose_name': 'Equipo',
                'verbose_name_plural': 'Equipos',
            },
        ),
        migrations.CreateModel(
            name='PlayerSuspension',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('num_matches', models.PositiveIntegerField()),
                ('reason', models.TextField(blank=True)),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='football_system.player')),
            ],
            options={
                'verbose_name': 'Suspensión de Jugador',
                'verbose_name_plural': 'Suspensiones de Jugadores',
            },
        ),
        migrations.AddField(
            model_name='player',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='football_system.team'),
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('local_team_image', models.ImageField(blank=True, null=True, upload_to='match_images/')),
                ('visiting_team_image', models.ImageField(blank=True, null=True, upload_to='match_images/')),
                ('recognition_local_team_image', models.ImageField(blank=True, null=True, upload_to='recognition_match_images/')),
                ('recognition_visiting_team_image', models.ImageField(blank=True, null=True, upload_to='recognition_match_images/')),
                ('date', models.DateTimeField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='football_system.footballcategory')),
                ('local_team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='local_matches', to='football_system.team')),
                ('visiting_team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='visiting_matches', to='football_system.team')),
            ],
            options={
                'verbose_name': 'Partido',
                'verbose_name_plural': 'Partidos',
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('type', models.CharField(choices=[('TD', 'Director Técnico'), ('PR', 'Planillero'), ('CU', 'Usuario')], default='CU', max_length=2, verbose_name='tipo')),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='profile_pictures/', verbose_name='foto de perfil')),
                ('club', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='football_system.club')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Persona',
                'verbose_name_plural': 'Personas',
                'abstract': False,
                'swappable': 'AUTH_USER_MODEL',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]

from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views_login

from .views import generic_views
from .views import create as views_create
from .views import list as views_list
from .views import update as views_update
from .views import delete as views_delete

urlpatterns = [
    path('', views_login.home, name='home'),
    path('login/', views_login.login_view, name='login'),
    path('logout/', views_login.logout_view, name='logout'),
    path('signup/', views_login.signup, name='signup'),
    path('check_email/', views_login.check_email, name='check_email'),
    path('check_username/', views_login.check_username, name='check_username'),
    path('profile/', views_login.profile, name='profile'),

    path('club/', generic_views.views_clubs, name='clubs'),

    path('teams/', views_list.TeamListView.as_view(), name='team_list'),
    path('teams/create/', views_create.TeamCreateView.as_view(), name='team_create'),
    path('teams/<int:pk>/update/', views_update.TeamUpdateView.as_view(), name='team_update'),
    path('teams/<int:pk>/delete/', views_delete.TeamDeleteView.as_view(), name='team_delete'),

    path('matches/', views_list.MatchListView.as_view(), name='match_list'),
    path('matches/create/', views_create.MatchCreateView.as_view(), name='match_create'),
    path('matches/<int:pk>/update/', views_update.MatchUpdateView.as_view(), name='match_update'),
    path('matches/<int:pk>/delete/', views_delete.MatchDeleteView.as_view(), name='match_delete'),

    path('players/', views_list.PlayerListView.as_view(), name='player_list'),
    path('players/create/', views_create.PlayerCreateView.as_view(), name='player_create'),
    path('players/<int:pk>/update/', views_update.PlayerUpdateView.as_view(), name='player_update'),
    path('players/<int:pk>/delete/', views_delete.PlayerDeleteView.as_view(), name='player_delete'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
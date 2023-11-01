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

    path('matches/', generic_views.views_matches, name='matches'),
    path('clubs/', generic_views.views_clubs, name='clubs'),

    # path('club/', views_list.ClubListView.as_view(), name='clubs'),
    # path('club/create/', views_create.ClubCreateView.as_view(), name='club_create'),
    # path('club/<int:pk>/update/', views_update.ClubUpdateView.as_view(), name='club_update'),
    # path('club/<int:pk>/delete/', views_delete.ClubDeleteView.as_view(), name='club_delete'),

    # path('person/', views_list.PersonListView.as_view(), name='person_list'),
    # path('person/create/', views_create.PersonCreateView.as_view(), name='person_create'),
    # path('person/<int:pk>/update/', views_update.PersonUpdateView.as_view(), name='person_update'),
    # path('person/<int:pk>/delete/', views_delete.PersonDeleteView.as_view(), name='person_delete'),

    # path('football-category/', views_list.FootballCategoryListView.as_view(), name='football_category_list'),
    # path('football-category/create/', views_create.FootballCategoryCreateView.as_view(), name='football_category_create'),
    # path('football-category/<int:pk>/update/', views_update.FootballCategoryUpdateView.as_view(), name='football_category_update'),
    # path('football-category/<int:pk>/delete/', views_delete.FootballCategoryDeleteView.as_view(), name='football_category_delete'),

    # path('team/', views_list.TeamListView.as_view(), name='team_list'),
    # path('team/create/', views_create.TeamCreateView.as_view(), name='team_create'),
    # path('team/<int:pk>/update/', views_update.TeamUpdateView.as_view(), name='team_update'),
    # path('team/<int:pk>/delete/', views_delete.TeamDeleteView.as_view(), name='team_delete'),

    path('match/', views_list.MatchListView.as_view(), name='matches'),
    path('match/create/', views_create.MatchCreateView.as_view(), name='match_create'),
    path('match/<int:pk>/update/', views_update.MatchUpdateView.as_view(), name='match_update'),
    path('match/<int:pk>/delete/', views_delete.MatchDeleteView.as_view(), name='match_delete'),

    # path('player/', views_list.PlayerListView.as_view(), name='players'),
    # path('player/create/', views_create.PlayerCreateView.as_view(), name='player_create'),
    # path('player/<int:pk>/update/', views_update.PlayerUpdateView.as_view(), name='player_update'),
    # path('player/<int:pk>/delete/', views_delete.PlayerDeleteView.as_view(), name='player_delete'),

    # path('player-suspension/', views_list.PlayerSuspensionListView.as_view(), name='player_suspension_list'),
    # path('player-suspension/create/', views_create.PlayerSuspensionCreateView.as_view(), name='player_suspension_create'),
    # path('player-suspension/<int:pk>/update/', views_update.PlayerSuspensionUpdateView.as_view(), name='player_suspension_update'),
    # path('player-suspension/<int:pk>/delete/', views_delete.PlayerSuspensionDeleteView.as_view(), name='player_suspension_delete'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
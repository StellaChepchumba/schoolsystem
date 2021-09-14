from django.urls import path
from .views import register_trainer, trainer_list,edit_trainer,trainer_profile



urlpatterns=[
    path('register/',register_trainer,name='register_trainer'),
    path('trainer_list/',trainer_list,name='trainer_list'),
    path('profile/<int:id>/',trainer_profile,name='trainer_profile'),
    path("edit/<int:id>/",edit_trainer,name="edit_trainer"),
]

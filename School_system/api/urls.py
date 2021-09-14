from django.urls import include,path
from rest_framework import routers, urlpatterns
from .views import CalenderViewset, CoursesViewset, StudentViewset, TrainerViewset


router=routers.DefaultRouter()
router.register (r"students",StudentViewset)
router.register (r"trainers",TrainerViewset)
router.register (r"courses",CoursesViewset)
router.register (r"calender",CalenderViewset)


urlpatterns=[
    path("",include(router.urls)),
]

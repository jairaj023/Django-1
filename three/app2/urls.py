from django.urls import path

from app2.views import one, two, three


urlpatterns = [
    path("one/", one, name="One page"),
    path("two/", two, name="Two Page"),
    path("three/", three, name="Three Page"),
]
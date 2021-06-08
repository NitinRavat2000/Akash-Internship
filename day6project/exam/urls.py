from django.conf.urls import url
from exam import views



urlpatterns = [
    url('test',views.showTest),
    url('result',views.showResult),




]

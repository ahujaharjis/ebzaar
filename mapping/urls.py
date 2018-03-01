from django.conf.urls import url

from . import views

app_name = 'mapping'
urlpatterns = [
    url(r'^get_changed_items/$',views.home,name="home"),
    url(r'^get_results/$',views.results,name="results"),

 ]
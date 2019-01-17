from django.urls import path, re_path


from .views import TemperatureView, TemperatureViewForm

app_name = 'temperature'
urlpatterns = [
    path(r"", TemperatureView.as_view()),
    path(r"update/", TemperatureViewForm.as_view()),
]

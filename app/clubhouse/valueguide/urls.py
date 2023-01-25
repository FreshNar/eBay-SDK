from django.urls import path
from .views import ValueGuideView, appraise

urlpatterns = [
    path('', ValueGuideView.as_view(), name='index'),
    path('value/', appraise, name='value'),
]

from django.urls import path
from .views import TestCreateView, SaveIQResultView, SaveEQResultView, ShowResultsView

urlpatterns = [
    path('test/', TestCreateView.as_view(), name='test-create'),
    path('result/iq/', SaveIQResultView.as_view(), name='iq-result-create'),
    path('result/eq/', SaveEQResultView.as_view(), name='eq-result-create'),
    path('results/<str:pk>/', ShowResultsView.as_view(), name='test-results'),
]
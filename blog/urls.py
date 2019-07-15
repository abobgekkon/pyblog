from django.urls import path
from .views import main, by_rubric, post_detail

app_name = 'blog'

urlpatterns = [
    path('', main, name='main'),
    path('<int:rubric_id>/', by_rubric, name='by_rubric'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', post_detail,
            name='post_detail'),
]
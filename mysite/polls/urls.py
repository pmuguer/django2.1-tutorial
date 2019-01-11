from django.urls import path

from polls import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('your-name/', views.get_name, name='your-name'),
    path('thanks/', views.thanks, name='thanks'),
    path('contact-form/', views.contact_form, name='contact-form')
]
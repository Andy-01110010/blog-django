from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]


"""We mapped general URL patterns for our views using the path function. The first pattern takes an empty string denoted by ' ' and returns the result generated from the PostList view which is essentially a list of posts for our homepage and at last we have an optional parameter name which is basically a name for the view which will later be used in the templates.

Names are an optional parameter, but it is a good practice to give unique and rememberable names to views which makes our work easy while designing templates and it helps keep things organized as your number of URLs grows.

Next, we have the generalized expression for the PostDetail views which resolve the slug (a string consisting of ASCII letters or numbers) Django uses angle brackets < > to capture the values from the URL and return the equivalent post detail page."""
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.render_index),
    url(r'^create-post/', views.render_edit_blog_post),
    url(r'^edit-post/([0-9]+)', views.render_edit_blog_post),
    url(r'^posts/([0-9]+)/?$', views.render_blog_post),

    # API Views
    url(r'^api/posts/([0-9]+)?', views.BlogPostViewSet.as_view()),

]
from django.conf.urls import url
from json_app import json_app_request

urlpatterns = [


    # GET    /posts
    # GET    /posts/0
    # POST   /posts
    # PATCH  /posts/1
    # DELETE /posts/1

    url(r'^$', json_app_request.postCurdAPI.as_view(), name="entity_url"),

    url(r'^(?P<entity>\w+)$', json_app_request.postCurdAPI.as_view(), name="entity_and_id"),
    url(r'^(?P<entity>\w+)/(?P<pk>\d+)$', json_app_request.postCurdAPI.as_view(), name="entity_and_id"),
]
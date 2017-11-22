from django.conf.urls import url, include

from . import views

course_patterns = [

    url(r'^list/$',
        views.CourseList.as_view(),
        name='list'),

    url(r'^(?P<pk>[0-9]+)/$',
        views.CourseDetail.as_view(),
        name='detail'),

    url(r'^add/$',
        views.CourseAdd.as_view(),
        name='add'),

    url(r'^edit/(?P<pk>[0-9]+)/$',
        views.CourseEdit.as_view(),
        name='edit'),

]

materials_patterns = [
    url(r'^list/$',
        views.MaterialList.as_view(),
        name='list'),

    url(r'^add/$',
        views.MaterialAdd.as_view(),
        name='add'),

    url(r'^delete/(?P<pk>[0-9]+)/$',
        views.MaterialDelete.as_view(),
        name='delete'),
]


urlpatterns = [

    url(r'^course/',
        include(course_patterns,
                namespace='course')),

    url(r'^course/(?P<course_pk>[0-9]+)/material/',
        include(materials_patterns,
                namespace='material')),

]

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

urlpatterns = [

    url(r'^course/',
        include(course_patterns,
                namespace='course')),
]

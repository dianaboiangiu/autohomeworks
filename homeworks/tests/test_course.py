from django.core.urlresolvers import reverse
from django.test import TestCase

from homeworks.tests.base.factories import CourseFactory


class CourseTests(TestCase):

    def setUp(self):
        super().setUp()
        self.course = CourseFactory()
        self.user = self.course.created_by
        self._DATA = {
            'name': 'TEST course',
            'description': 'Description course',
        }

    def test_list_courses(self):
        self.client.force_login(self.user)
        resp = self.client.get(reverse('course:list'),
                               follow=True)
        self.assertEqual(resp.status_code, 200)
        courses_count = resp.context['courses'].count()
        self.assertEqual(courses_count, 1)

    def test_detail_course(self):
        self.client.force_login(self.user)
        resp = self.client.get(
            reverse('course:detail',
                    kwargs={'pk': self.course.pk}),
            follow=True)
        self.assertEqual(resp.status_code, 200)
        course = resp.context['course']
        self.assertEqual(course.name, self.course.name)
        self.assertEqual(course.description, self.course.description)
        self.assertEqual(course.created_by, self.course.created_by)

    def test_create_course(self):
        self.client.force_login(self.user)
        resp = self.client.post(reverse('course:add'), self._DATA,
                                follow=True)
        self.assertEqual(resp.status_code, 200)
        courses_count = resp.context['courses'].count()
        self.assertEqual(courses_count, 2)

    def test_edit_course(self):
        self.client.force_login(self.user)
        resp = self.client.post(reverse('course:edit',
                                        kwargs={'pk': self.course.pk}),
                                self._DATA,
                                follow=True)
        self.assertEqual(resp.status_code, 200)
        course = resp.context['course']
        self.assertEqual(course.name, self._DATA['name'])
        self.assertEqual(course.description, self._DATA['description'])

from django.core.urlresolvers import reverse
from django.test import TestCase

from homeworks.tests.base.factories import CourseFactory, MaterialFactory


class MaterialTests(TestCase):

    def setUp(self):
        super().setUp()
        self.course = CourseFactory()
        self.material = MaterialFactory(course=self.course)
        self.material2 = MaterialFactory(course=self.course)
        self.user = self.course.created_by
        self._DATA = {
            'course': self.course.id,
        }

    def test_list_materials(self):
        self.client.force_login(self.user)
        resp = self.client.get(
            reverse('material:list',
                    kwargs={'course_pk': self.course.pk}),
            follow=True)
        self.assertEqual(resp.status_code, 200)
        courses_count = resp.context['materials'].count()
        self.assertEqual(courses_count, 2)
        self.assertEqual(resp.context["materials"][0].pk, self.material.pk)
        self.assertEqual(resp.context["materials"][1].pk, self.material2.pk)

    def test_delete_material(self):
        self.client.force_login(self.user)
        resp = self.client.post(reverse('material:delete',
                                        kwargs={'course_pk': self.course.pk,
                                                'pk': self.material.pk,
                                                }), follow=True)
        self.assertEqual(resp.status_code, 200)
        materials = resp.context['materials']
        self.assertEqual(materials.count(), 1)

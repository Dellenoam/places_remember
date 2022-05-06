from django.test import TestCase
from django.contrib.auth.models import User
from memories.forms import MemoriesForm
from memories.models import Memories


class TestForms(TestCase):

    def setUp(self):
        self.user = User.objects.create(
            username='TestUserName',
            password='TestUserPassword',
            is_active=True,
            is_staff=False,
            is_superuser=False,
        )

    def test_memories_form_valid_data(self):
        test_user_memory = MemoriesForm(
            data={
                'title': 'TestTitle',
                'description': 'TestDescription',
                'location': 'TestLocation'
            })

        self.assertTrue(test_user_memory.is_valid())

    def test_memories_form_save_data(self):
        test_user_memory = MemoriesForm(
            data={
                'title': 'TestTitle',
                'description': 'TestDescription',
                'location': 'TestLocation'
            })

        test_user_memory.is_valid()
        instance = test_user_memory.save(commit=False)
        instance.user = self.user
        instance.save()

        self.assertEquals(Memories.objects.first().title, 'TestTitle')
        self.assertEquals(Memories.objects.first().description, 'TestDescription')
        self.assertEquals(Memories.objects.first().location, 'TestLocation')

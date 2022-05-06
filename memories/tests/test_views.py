from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from memories.models import Memories
from memories.views import my_memories, new_memory


class TestViews(TestCase):
    def test_my_memories_login_required(self):
        response = self.client.get(reverse(my_memories))

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home') + '?next=/my-memories/')

    def test_new_memory_login_required(self):
        response = self.client.get(reverse(new_memory))

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home') + '?next=/new-memory/')

    def test_my_memories_logged_in_GET(self):
        self.client.force_login(User.objects.get_or_create(username='TestUserName')[0])

        response = self.client.get(reverse(my_memories))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'memories/my_memories.html')

    def test_new_memory_logged_in_GET(self):
        self.client.force_login(User.objects.get_or_create(username='TestUserName')[0])

        response = self.client.get(reverse(new_memory))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'memories/new_memory.html')

    def test_new_memory_logged_in_POST(self):
        self.client.force_login(User.objects.get_or_create(username='TestUserName')[0])
        response = self.client.post(
            reverse('new_memory'),
            {
                'title': 'TestTitle',
                'description': 'TestDescription',
                'location': 'TestLocation',
            }
        )

        self.assertEquals(response.status_code, 302)
        self.assertEquals(Memories.objects.first().title, 'TestTitle')

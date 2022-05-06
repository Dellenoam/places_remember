from django.test import TestCase
from django.urls import reverse, resolve
from memories.views import my_memories, new_memory


class TestUrls(TestCase):

    def test_my_memories_url_resolves(self):
        url = reverse('my_memories')
        self.assertEquals(resolve(url).func, my_memories)

    def test_new_memory_url_resolves(self):
        url = reverse('new_memory')
        self.assertEquals(resolve(url).func, new_memory)

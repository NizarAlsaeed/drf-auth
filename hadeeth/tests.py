from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Hadeeth
# Create your tests here.

class HadeethModelTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_user = get_user_model().objects.create_user(username='tester',password='pass')
        test_user.save()

        test_hadeeth = Hadeeth.objects.create(
            content = 'test0',
            uploaded_by = test_user,
            book = 'test1',
            narrator = 'test2'
        )
        test_hadeeth.save()

    def test_blog_content(self):
        hadeeth = Hadeeth.objects.get(id=1)

        self.assertEqual(str(hadeeth.uploaded_by), 'tester')
        self.assertEqual(hadeeth.content, 'test0')
        self.assertEqual(hadeeth.book, 'test1')
        self.assertEqual(hadeeth.narrator, 'test2')

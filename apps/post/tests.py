from django.test import TestCase
from rest_framework.test import APITestCase
from .models import Post
from django.utils import timezone
import json

# Create your tests here.

class PostAPITestCase(APITestCase):
    def test_create_post_via_api(self):
        EXPECTED_TITLE = "flkadflsdkfjlksdjf"
        EXPECTED_DESCRIPTION = "847130p849psd8ya9psifgh24oirWRCQH$TC$N"

        response = self.client.post(
            "/api/posts/",
            {
                'title': EXPECTED_TITLE,
                'description': EXPECTED_DESCRIPTION,
            },
            format='json'
        )
        now = timezone.now()
        self.assertEqual(response.status_code, 200)
        response_object = json.loads(response.content.decode())
        post_id = response_object['id']

        post = Post.objects.get(id=post_id)

        self.assertEqual(post.title, EXPECTED_TITLE)
        self.assertEqual(post.description, EXPECTED_DESCRIPTION)

        # has the possibility of failing if the computer you run tests on is really slow
        self.assertAlmostEqual(now, post.created_date, delta=timezone.timedelta(seconds=2))


    def test_edit_post_via_api(self):
        EXPECTED_TITLE = "correct title"
        EXPECTED_DESCRIPTION = "correct description"

        post = Post.objects.create(title='wrong title', description='wrong description')

        response = self.client.put(
            "/api/posts/{}".format(post.id),
            {
                'title': EXPECTED_TITLE,
                'description': EXPECTED_DESCRIPTION,
            },
            format='json'
        )

        self.assertEqual(response.status_code, 200)

        post.refresh_from_db()

        self.assertEqual(post.title, EXPECTED_TITLE)
        self.assertEqual(post.description, EXPECTED_DESCRIPTION)



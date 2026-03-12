from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from ..models import LiteraryFormat

LITERARY_FORMAT_URL = reverse("catalog:literary-formats-list")


class PublicLiteraryFormatTest(TestCase):
    # def setUp(self) -> None:
    #     self.client = Client()

    """
    Lines above are redundant
    if we do not log in no need for
    overwriting bult in funcs
    """

    def test_login_required(self):
        res = self.client.get(LITERARY_FORMAT_URL)
        self.assertNotEqual(res.status_code, 200)


class PrivateLiteraryFormatTest(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="test_username",
            password="test_password",
        )
        self.client.force_login(self.user)

    def test_retrieve_literary_formats(self):
        LiteraryFormat.objects.create(name="drama")
        LiteraryFormat.objects.create(name="poetry")
        res = self.client.get(LITERARY_FORMAT_URL)

        self.assertEqual(res.status_code, 200)
        literary_formats = LiteraryFormat.objects.all()

        self.assertEqual(
            list(res.context["literary_format_list"]),
            list(literary_formats)
        )
        self.assertTemplateUsed(res, "catalog/literary_format_list.html")


class PrivateAuthorTests(TestCase):

    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="test",
            password="password123"
        )

        self.client.force_login(self.user)

    def test_create_author(self):
        form_data = {
            "username": "new_user",
            "password1": "user12test",
            "password2": "user12test",
            "first_name": "Test first",
            "last_name": "Test last",
            "pseudonym": "Test Pseudonym",
        }

        self.client.post(reverse("catalog:author-create"), data=form_data)
        new_user = get_user_model().objects.get(username=form_data["username"])

        self.assertEqual(new_user.first_name, form_data["first_name"])
        self.assertEqual(new_user.last_name, form_data["last_name"])
        self.assertEqual(new_user.pseudonym, form_data["pseudonym"])

from django.contrib.auth import get_user_model
from django.test import TestCase

from catalog.models import LiteraryFormat, Book


class ModelTests(TestCase):
    def test_literary_format_str(self):
        literary_format = LiteraryFormat.objects.create(name="test")
        self.assertEqual(str(literary_format), literary_format.name)

    def test_author_str(self):
        author = get_user_model().objects.create(
            first_name="test1",
            last_name="test2",
            username="test_username",
            password="test_password"
        )
        self.assertEqual(str(author), f"{author.first_name} {author.last_name}")

    def test_book_str(self):
        literary_format = LiteraryFormat.objects.create(name="test")
        book = Book.objects.create(title="test", price=10.3, format=literary_format)
        self.assertEqual(
            str(book),
            f"{book.title} (price: {book.price}, format: {book.format})",
        )

    def test_create_author_with_pseudonym(self):
        username = "test_username"
        password = "test_password"
        pseudonym = "test_pseudonym"
        author = get_user_model().objects.create_user(
            first_name="test1",
            last_name="test2",
            username=username,
            password=password,
            pseudonym=pseudonym,
        )
        self.assertEqual(author.username, username)
        self.assertEqual(author.pseudonym, pseudonym)
        self.assertTrue(author.check_password(password))
from django.test import TestCase

from catalog.forms import AuthorCreationForm


class FormsTests(TestCase):
    def test_author_creation_form_with_pseudonym_first_last_name_is_valid(self):
        form_data = {
            "username": "new_user",
            "password1": "user12test",
            "password2": "user12test",
            "first_name": "test first",
            "last_name": "test last",
            "pseudonym": "test pseudonym",
        }
        form = AuthorCreationForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)

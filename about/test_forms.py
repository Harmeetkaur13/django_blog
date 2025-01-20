from django.test import TestCase
from .forms import CollaborateForm


class TestCollaborateForm(TestCase):

    def test_form_is_valid(self):
        """ Test for all fields"""
        form = CollaborateForm({
            'name': 'John Doe',
            'email': 'test@test.com',
            'message': 'Hello!'
        })
        self.assertTrue(form.is_valid(), msg="Form is not valid")
    def test_form_is_not_valid_without_name(self):
        """ Test form is not valid without name """
        form = CollaborateForm({
            'name': '',
            'email': 'test@test.com',
            'message': 'Hello!'
        })
        self.assertFalse(form.is_valid(), msg="Form should not be valid without name")

    def test_form_is_not_valid_without_email(self):
        """ Test form is not valid without email """
        form = CollaborateForm({
            'name': 'John Doe',
            'email': '',
            'message': 'Hello!'
        })
        self.assertFalse(form.is_valid(), msg="Form should not be valid without email")

    def test_form_is_not_valid_without_message(self):
        """ Test form is not valid without message """
        form = CollaborateForm({
            'name': 'John Doe',
            'email': 'test@test.com',
            'message': ''
        })
        self.assertFalse(form.is_valid(), msg="Form should not be valid without message")    
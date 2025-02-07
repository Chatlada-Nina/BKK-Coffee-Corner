from django.test import TestCase
from .forms import CommentForm, CreateForum


class TestCommentForm(TestCase):

    def test_form_is_valid(self):
        comment_form = CommentForm({'body': 'This is a great comment'})
        self.assertTrue(comment_form.is_valid(), msg='Form is not valid')

    def test_form_is_invalid(self):
        comment_form = CommentForm({'body': ''})
        self.assertFalse(comment_form.is_valid(), msg="Form is valid")


class TestCreateForumForm(TestCase):

    def test_form_is_valid(self):
        """ Test for all fields"""
        form = CreateForum({
            'title': 'The Best Coffee in Bangkok',
            'slug': 'the-best-coffee-in-bangkok',
            'content': 'The Coffee Corner is the best!'
        })
        self.assertTrue(form.is_valid(), msg="Form is not valid")

    def test_title_is_required(self):
        """Test for the 'title' field"""
        form = CreateForum({
            'title': '',
            'slug': 'the-best-coffee-in-bangkok',
            'content': 'The Coffee Corner is the best!'
        })
        self.assertFalse(
            form.is_valid(),
            msg="Title was not provided, but the form is valid"
        )

    def test_email_is_required(self):
        """Test for the 'slug' field"""
        form = CreateForum({
            'title': 'The Best Coffee in Bangkok',
            'slug': '',
            'content': 'The Coffee Corner is the best!'
        })
        self.assertFalse(
            form.is_valid(),
            msg="Slug was not provided, but the form is valid"
        )

    def test_message_is_required(self):
        """Test for the 'content' field"""
        form = CreateForum({
            'title': 'The Best Coffee in Bangkok',
            'slug': 'the-best-coffee-in-bangkok',
            'content': ''
        })
        self.assertFalse(
            form.is_valid(),
            msg="Content was not provided, but the form is valid"
        )

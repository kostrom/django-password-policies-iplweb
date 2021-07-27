from django.test import TestCase
from django.http import HttpRequest
from password_policies.context_processors import password_status

class ContextProcessorsTests(TestCase):

    def test_password_status(self):
        request = HttpRequest()
        request.user = None
        try:
            self.assertEqual({}, password_status(request))
        except:
            self.fail("unhandled exception in password_status")

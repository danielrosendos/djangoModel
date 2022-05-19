from django.test import TestCase

from ...Models.UserModel import UserModel

class CreateUserTest(TestCase):
    def setUp(self) -> None:
        UserModel.objects.create(
            username="sport123",
            password="123",
            email="daniel@hot.com.br"
        )

    def test_create_user(self):
        user = UserModel.objects.get(username="sport123")
        self.assertEqual(user.username, "sport123")
        self.assertEqual(user.password, "123")
        self.assertEqual(user.email, "daniel@hot.com.br")
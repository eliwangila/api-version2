# import unittest

# from app.models import User

# class UserTest(unittest.TestCase):
#     def setUp(self):
#         self.new_user = User(username='ekirapa', emails= "test@test.com", bio ='default bio',password='blindspot1')

#     def test_password_setter(self):
#         self.assertTrue(self.new_user.hashed_password is not None)

#     def test_no_access_password(self):
#         with self.assertRaises(AttributeError):
#             self.new_user.hashed_password

#     def test_password_verification(self):
#         self.assertTrue(self.new_user.verify_password('blindspot1'))


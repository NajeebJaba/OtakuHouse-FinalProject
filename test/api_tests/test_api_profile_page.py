import unittest
from logic.api_logic.api_profile_page import ProfilePage

"""Before start testing , I want to tell that the profile form didn't change any 
                    value ,and the update button didn't work and get error 500, but actually if I updating
                     the username for example, it's appear in homePage with the new username updating, same thing for password
                      and email, when user do login actions he will see the updating"""


class TestProfilePage(unittest.TestCase):

    def setUp(self):
        self.UserProfile = ProfilePage()
        self.response = None
        self.data = None

    """When entering to profile page , in the form there is email to change"""

    def test_change_the_profile_form_email_for_user(self):
        self.response = self.UserProfile.profile_page_refresh(self.UserProfile.user_id, self.UserProfile.Username,
                                                              self.UserProfile.email_for_reg, self.UserProfile.UserPassword)
        self.assertEqual(self.response.status_code, 200)

    """When entering to profile page , in the form there is password and confirm password to change"""

    # confirm password should be match with password,otherwise the form will not change
    def test_change_profile_form_password_for_user(self):
        self.response = self.UserProfile.profile_page_refresh(self.UserProfile.user_id, self.UserProfile.Username,
                                                              self.UserProfile.UserEmail, self.UserProfile.updating_password)
        self.assertEqual(self.response.status_code, 200)

    """When entering to profile page , in the form there is name for user that display in HomePage"""

    # Also here I can change the name for the user
    def test_change_profile_form_name_user(self):
        self.response = self.UserProfile.profile_page_refresh(self.UserProfile.user_id, self.UserProfile.change_name,
                                                              self.UserProfile.UserEmail, self.UserProfile.UserPassword)
        self.assertEqual(self.response.status_code, 200)

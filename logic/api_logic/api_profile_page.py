from infra.api_infra.api_wrapper import APIWrapper


class ProfilePage(APIWrapper):
    def __init__(self):
        super().__init__()
        self.json = None

    def profile_page_refresh(self, user_id, user_name, user_mail, user_password):
        self.json_data = {"id": user_id, "name": user_name,
                          "email": user_mail, "password": user_password}

        print(f"About to update profile for user ID: {user_id}")
        print(f"Updating to: Name - {user_name}, Email - {user_mail}")

        self.response = self.request.put(f'{self.url[:-2]}api/users/profile/update/', json=self.json_data,
                                         headers=self.headersUpdate)

        print(f'Profile updated. Response status code: {self.response.status_code}')
        print(f'Updated data: {self.response.json()}')

        return self.response

from infra.api_infra.api_browser_wrapper import APIBrowserWrapper

class APIProfilePage:
    def __init__(self, api_browser_wrapper):
        self.api_browser_wrapper = api_browser_wrapper

    def update_profile(self, user_id, profile_data, headers):
        endpoint = f"api/users/{user_id}/profile/update"
        response = self.api_browser_wrapper.put(endpoint, profile_data, headers)
        return response

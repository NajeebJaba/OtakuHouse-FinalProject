import requests
from infra.api_infra.api_config_handler import APIConfigHandler


class APIWrapper:

    def __init__(self):
        self.response = None
        self.myHandler = APIConfigHandler()
        self.config = self.myHandler.read_config_data()
        """the website is local so the url is look different: http://127.0.0.1:8000/#/ """
        self.url = self.config['url']
        self.Username = self.config['user_name_for_profile']
        self.UserEmail = self.config['email_for_login_page']
        self.UserPassword = self.config['password_for_log_page']
        self.search_product_by_name = self.config['search_product_by_name'].lower()
        self.product_id = self.config['product_id']

        self.rate = self.config['rating_product']
        self.review_comment = self.config['review_comment']
        self.order_id_or = self.config['orderID']
        self.user_id = self.config['userId']
        self.request = requests
        self.change_name = self.config['new_username']
        self.email_for_reg = self.config['email_for_register_and_update_use_email']
        self.updating_password = self.config['update_password']

        """I called it from json"""
        # self.token = self.config['tokens']['defaultToken']['value']
        # self.headers = self.config['tokens']['defaultToken']['headers']
        # self.token2 = self.config['tokens']['alternateToken']['value']
        # self.headers2 = self.config['tokens']['alternateToken']['headers']
        # self.updateProfileToken = self.config['tokens']['updateProfileToken']['value']
        # self.headersUpdate = self.config['tokens']['updateProfileToken']['headers']

        self.token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzEzNzA3MDczLCJqdGkiOiI2MTVhNWM1MTljOGQ0MmFjODM4YWI0MGExYzg2YTE2ZSIsInVzZXJfaWQiOjh9.dpK02iVtvtLn2VeZkFRngY4pWzYvGzUj34F1uYZRJis"
        self.headers = {
            "Authorization": f"Bearer {self.token}"
        }
        self.token2 = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzEzNzEyOTE5LCJqdGkiOiI5MGQ3NmJhM2Q1YTg0MTE4ODFiN2UxZGNmODllMGI0YiIsInVzZXJfaWQiOjh9.JmN9m1-qwAduAGmA7XGuoFERJvCdQLhf_XHqeIu5IEA"
        self.headers2 = {
            "Authorization": f"Bearer {self.token2}"
        }
        self.updateProfileToken = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzEzNzk3NzgxLCJqdGkiOiI1MjFjYTM5MWIxODE0ZDkyYjhiMDZjMjZjYWVhMjY2MyIsInVzZXJfaWQiOjh9.N2DQiPUUNLlvR1i2bD5oY8rVdcohs764X2qRe67KRXo"
        self.headersUpdate = {
            "Authorization": f"Bearer {self.updateProfileToken}"
        }



    def api_get_request(self, url):
        self.response = self.request.get(url)
        return self.response

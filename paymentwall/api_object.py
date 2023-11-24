import re
from .base import Paymentwall

class ApiObject(Paymentwall):
    def check_project_env(self):
        reg = re.compile(r'_+')
        return reg.search(self.secret_key) is not None

    def create_post_options(self, url, path, method):
        # Set the request options
        post_options = {
            'host': url,
            'path': path,
            'method': method,
            'headers': {
                'Content-Type': 'application/x-www-form-urlencoded',
                'X-ApiKey': self.secret_key
            }
        }
        return post_options

    def create_request(self, type, additional_path=None):
        additional_path = additional_path or ''
        if not self.check_project_env() and type == "onetimetoken":
            method = "POST"
            url = self.BRICK_ONETIMETOKEN_TEST_BASE_URL
            path = self.BRICK_ONETIMETOKEN_TEST_PATH
        else:
            url = self.BRICK_BASE_URL
            method = "POST"
            if type == "onetimetoken":
                path = self.BRICK_ONETIMETOKEN_PATH
            elif type == "charge":
                path = self.BRICK_CHARGE_PATH + additional_path
            elif type == "subscription":
                path = self.BRICK_SUBSCRIPTION_CHARGE_PATH + additional_path

        post_options = self.create_post_options(url, path, method)
        return post_options
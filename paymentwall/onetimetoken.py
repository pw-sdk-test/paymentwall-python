from .api_object import ApiObject
from .card import Card
from .http_action import HttpAction
from urllib.parse import urlencode

class Onetimetoken(ApiObject):
    def __init__(self, number=None, exp_month=None, exp_year=None, cvv=None):
        self.card = Card(number, exp_month, exp_year, cvv)

    def create_onetimetoken(self):
        post_data = {
            'public_key': self.app_key,
            'card[number]': self.card.number,
            'card[exp_month]': self.card.exp_month,
            'card[exp_year]': self.card.exp_year,
            'card[cvv]': self.card.cvv
        }

        post_data = urlencode(post_data).encode('utf-8')
        post_options = self.create_request('onetimetoken')
        http_action = HttpAction()
        return http_action.run_action(post_options, post_data, True)
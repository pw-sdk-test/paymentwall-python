from .http_action import HttpAction
from .api_object import ApiObject
from urllib.parse import urlencode

class Charge(ApiObject):
    def __init__(self, amount=None, currency='USD', description=None, email=None, fingerprint=None, token=None, extra=None):
        self.amount = amount
        self.currency = currency
        self.description = description
        self.email = email
        self.fingerprint = fingerprint
        self.token = token
        self.extra = extra

    def create_charge(self):
        post_data = {
            'public_key': self.app_key,
            'amount': self.amount,
            'currency': self.currency,
            'description': self.description,
            'email': self.email,
            'fingerprint': self.fingerprint,
            'token': self.token
        }

        if self.extra:
            post_data.update(self.extra)

        post_data = urlencode(post_data).encode('utf-8')

        post_options = self.create_request('charge')
        http_action = HttpAction()
        return http_action.run_action(post_options, post_data, True)

    def other_operation(self, charge_id, operation_type):
        post_data = ''
        additional_path = ''

        if operation_type == 'detail':
            additional_path = f'/{charge_id}'
        elif operation_type == 'refund':
            additional_path = f'/{charge_id}/refund'
        elif operation_type == 'capture':
            additional_path = f'/{charge_id}/capture'
        elif operation_type == 'void':
            additional_path = f'/{charge_id}/void'
        else:
            print('Parameter error in charge.other_operation')

        post_options = self.create_request('charge', additional_path)
        http_action = HttpAction()
        return http_action.run_action(post_options, post_data, True)
from .http_action import HttpAction
from .api_object import ApiObject
try: 
    from urllib.parse import urlencode
except ImportError:
    from urllib import urlencode

class Subscription(ApiObject):
    def __init__(self, amount=None, currency='USD', description=None, email=None, fingerprint=None, token=None, period=None, period_duration=None, trial_data=None, extra=None):
        self.amount = amount
        self.currency = currency
        self.description = description
        self.email = email
        self.fingerprint = fingerprint
        self.token = token
        self.period = period
        self.period_duration = period_duration
        self.trial_data = trial_data
        self.extra = extra

    def create_subscription(self):
        post_data = {
            'public_key': self.app_key,
            'amount': self.amount,
            'currency': self.currency,
            'description': self.description,
            'email': self.email,
            'fingerprint': self.fingerprint,
            'token': self.token,
            'period': self.period,
            'period_duration': self.period_duration
        }

        if self.trial_data:
            post_data.update(self.trial_data)

        if self.extra:
            post_data.update(self.extra)

        post_data = urlencode(post_data).encode('utf-8')

        post_options = self.create_request('subscription')
        http_action = HttpAction()
        return http_action.run_action(post_options, post_data, True)

    def other_operation(self, subscription_id, operation_type):
        post_data = ''
        additional_path = ''

        if operation_type == 'detail':
            additional_path = '/{}'.format(subscription_id)
        elif operation_type == 'cancel':
            additional_path = '/{}/cancel'.format(subscription_id)
        else:
            print('Parameter error in subscription.other_operation')

        post_options = self.create_request('subscription', additional_path)
        http_action = HttpAction()
        return http_action.run_action(post_options, post_data, True)

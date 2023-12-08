from .success import Success
from .err import Err

class CallbackRes:
    def __init__(self, JSON_chunk, String_chunk):
        self.JSON_chunk = JSON_chunk
        self.String_chunk = String_chunk

    def is_successful(self):
        if 'type' in self.JSON_chunk:
            return self.JSON_chunk['type'] != 'Error'

        if 'secure' in self.JSON_chunk:
            return True

        if 'object' in self.JSON_chunk:
            return self.JSON_chunk['object'] in ['charge', 'subscription']

        print(self.get_full_response())
        return False

    def is_captured(self):
        return Success().get_parameter('captured', self.JSON_chunk)

    def is_refunded(self):
        return Success().get_parameter('refunded', self.JSON_chunk)

    def is_activated(self):
        return Success().get_parameter('active', self.JSON_chunk)

    def is_started(self):
        return Success().get_parameter('started', self.JSON_chunk)

    def is_expired(self):
        return Success().get_parameter('expired', self.JSON_chunk)

    def is_trial(self):
        return 'trial' in self.JSON_chunk

    def is_under_review(self):
        return Success().get_parameter('risk', self.JSON_chunk)

    def is_under_3d_secure(self):
        return Success().get_parameter('secure', self.JSON_chunk)

    def get_full_response(self, type=None):
        if type == "JSON":
            return self.JSON_chunk
        else:
            return self.String_chunk

    def get_3d_html(self):
        secure = Success().get_parameter('secure', self.JSON_chunk)
        if secure and 'formHTML' in secure:
            return secure['formHTML']
        return None

    def get_3d_url(self):
        secure = Success().get_parameter('secure', self.JSON_chunk)
        if secure and 'redirect' in secure:
            return secure['redirect']
        return None

    def get_charge_id(self):
        if self.JSON_chunk['object'] == 'charge':
            return Success().get_parameter('id', self.JSON_chunk)
        charges = Success().get_parameter('charges', self.JSON_chunk)
        return charges[-1] if charges else None
    
    def get_onetime_token(self):
        return Success().get_parameter('token', self.JSON_chunk)

    def get_permanent_token(self):
        if 'card' in self.JSON_chunk and self.JSON_chunk['card']:
            card = Success().get_parameter('card', self.JSON_chunk)
            if card and 'token' in card:
                return card['token']
        return None

    def get_card_info(self):
        return Success().get_parameter('card', self.JSON_chunk)

    def get_trial_info(self):
        return Success().get_parameter('trial', self.JSON_chunk)

    def get_subscription_id(self):
        return Success().get_parameter('id', self.JSON_chunk)

    def get_error_code(self):
        return Err().get_parameter('code', self.JSON_chunk)

    def get_error_details(self):
        return Err().get_parameter('error', self.JSON_chunk)

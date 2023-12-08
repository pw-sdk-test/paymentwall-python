import json

try: 
    import http.client as httplib
except ImportError:
    import httplib

try: 
    from .response.abstract import CallbackRes
except ImportError:
    from response.abstract import CallbackRes

import ssl
import certifi

context = ssl.create_default_context(cafile=certifi.where())

class HttpAction:

    def run_action(self, post_options, post_data, https_action):
        if not https_action:
            post_options['port'] = 80
            conn = httplib.HTTPConnection(post_options['host'], context=context)
        else:
            post_options['port'] = 443
            conn = httplib.HTTPSConnection(post_options['host'], context=context)

        conn.request('POST', post_options['path'], post_data, post_options['headers'])

        response = conn.getresponse().read().decode('utf8')
        
        string_chunk = ""

        for chunk in response:
            string_chunk += chunk

        json_chunk = json.loads(string_chunk)

        return CallbackRes(json_chunk, string_chunk)

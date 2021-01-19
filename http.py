
# 发动http请求
# urllib
# requests

import json
import requests
from urllib import request
from urllib.parse import quote

# python2 经典类和新式类（显示继承object）的区别
# python3 新式类


class HTTP:

    @staticmethod
    def get(url, return_json=True):
        r = requests.get(url)
        # restful  json
        if r.status_code != 200:
            return {} if return_json else ''
        return r.json() if return_json else r.text

    def get_with_request(self, url, return_json=True):
        url = quote(url, safe='/:?=&')
        try:
            with request.urlopen(url) as r:
                result_str = r.read()
                result_str = str(result_str, encoding='utf-8')
            if return_json:
                return json.loads(result_str)
            else:
                return result_str
        except OSError as e:
            print(e.reason)
            if return_json:
                return {}
            else:
                return None
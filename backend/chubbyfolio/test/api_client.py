import json

from rest_framework.test import APIClient


class DRFClient(APIClient):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get(self, *args, **kwargs):
        __tracebackhide__ = True

        return self._api_call('get', kwargs.get('expected_status_code', 200), *args, **kwargs)

    def post(self, *args, **kwargs):
        __tracebackhide__ = True

        return self._api_call('post', kwargs.get('expected_status_code', 201), *args, **kwargs)

    def put(self, *args, **kwargs):
        __tracebackhide__ = True

        return self._api_call('put', kwargs.get('expected_status_code', 200), *args, **kwargs)

    def delete(self, *args, **kwargs):
        __tracebackhide__ = True

        return self._api_call('delete', kwargs.get('expected_status_code', 204), *args, **kwargs)

    def _api_call(self, method, expected, *args, **kwargs):
        __tracebackhide__ = True

        kwargs['format'] = kwargs.get('format', 'json')  # by default submit all data in JSON
        as_response = kwargs.pop('as_response', False)

        method = getattr(super(), method)
        response = method(*args, **kwargs)

        if as_response:
            return response

        content = self._decode(response)

        status = response.status_code
        assert response.status_code == expected, f'non-expected statuscode: {status}: {content}'

        return content

    def _decode(self, response):
        if not len(response.content):
            return

        content = response.content.decode('utf-8', errors='ignore')
        if 'application/json' in response._headers['content-type'][1]:
            return json.loads(content)
        else:
            return content

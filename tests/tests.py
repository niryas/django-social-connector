from http import HTTPStatus
from unittest.mock import patch

from django.shortcuts import reverse
from django.test import SimpleTestCase, override_settings

TOKEN_ENDPOINT = reverse("ig_auth")


@override_settings(DEBUG=True)
@patch("requests.post")
class IGTokenTests(SimpleTestCase):
    @override_settings(DEBUG=False)
    def test_returns_error_when_not_debug_mode(self, *mocks):
        resp = self.client.post(TOKEN_ENDPOINT)
        self.assertEqual(HTTPStatus.NOT_FOUND, resp.status_code)

    def test_rejects_without_code(self, *mocks):
        resp = self.client.post(
            TOKEN_ENDPOINT,
            {"uri": "http://localhost"},
            content_type="application/json",
        )

        self.assertEqual(resp.status_code, HTTPStatus.BAD_REQUEST)
        data = resp.json()
        self.assertEqual("noToken", data["errorCode"])

    def test_rejects_without_uri(self, *mocks):
        resp = self.client.post(
            TOKEN_ENDPOINT,
            {"code": "testcode"},
            content_type="application/json",
        )

        self.assertEqual(resp.status_code, HTTPStatus.BAD_REQUEST)
        data = resp.json()
        self.assertEqual("noRedirectUri", data["errorCode"])

    def test_rejects_get(self, *mocks):
        resp = self.client.get(TOKEN_ENDPOINT)

        assert resp.status_code == HTTPStatus.METHOD_NOT_ALLOWED

    def test_sends_data_to_api(self, mock_api):
        mock_api.return_value.json.return_value = {"test": "data"}
        mock_api.return_value.status_code = 200

        resp = self.client.post(
            TOKEN_ENDPOINT,
            {"code": "test_code", "uri": "http://localhost/"},
            content_type="application/json",
        )

        mock_api.assert_called_once()

        returned_data = resp.json()
        self.assertEqual("data", returned_data["test"])

        api_url, sent_data = mock_api.call_args.args
        self.assertIn("https://api.instagram.com", api_url)
        self.assertEqual("test_code", sent_data["code"])
        self.assertEqual("http://localhost/", sent_data["redirect_uri"])
        self.assertEqual("authorization_code", sent_data["grant_type"])

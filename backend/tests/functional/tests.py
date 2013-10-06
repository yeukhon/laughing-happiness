# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import json
import unittest
import requests

def request(method, url, data, headers={"content-type": "application/json"}):
    req = {"GET": requests.get,
        "POST": requests.post,
        "delete": requests.delete,
        "put": requests.put}
    r = req[method](url, data=json.dumps(data), headers=headers)
    return r

class TestLogin(unittest.TestCase):
    """
    def test_user_login_successful(self):
        data = {"audience": "foo@bar.com", "assertion": ""}
        r = request("POST", "http://127.0.0.1:5000/login", data)
        self.assertEqual(r.json()["content"], "Logged in.")
        self.assertEqual(r.status_code, 200)

    """

    pass

class TestUserViews(unittest.TestCase):
    def test_create_user(self):
        data = {"email": "foo@bar.com"}
        r = request("POST", "http://127.0.0.1:5000/users/register", data)
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["email"], data["email"])


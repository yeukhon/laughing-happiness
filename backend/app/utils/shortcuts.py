# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from flask import make_response

def abort(status_code, error, content_type="application/json"):
    """
    Return a HTTP response object of a specific status code
    with sepcific error. By default content_type is assumed
    to be application/json.

    Parameters
    ----------
    status_code : int
    error : iterable
        An error message to return. It could be a dictionary
        (for JSON) or a string (for plaintext).
        content_type : optional, str
        Default set to ``application/json``.

    Returns
    -------
    response : HTTPResponse

    """
    
    content_type = content_type.lower()
    if content_type == "application/json":
        return jsonify(error), status_code
    else:
        response = make_response()
        response.status = status_code
        response.set_header('content-type', content_type)
        return response

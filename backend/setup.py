# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from setuptools import setup

install_requires = [
    "flask==0.10.1",
    "requests==2.0.0",
]

setup(name="laughing-happiness",
    version="0.0",
    description="",
    install_requires=install_requires,
)


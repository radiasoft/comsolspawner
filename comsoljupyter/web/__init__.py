# -*- coding: utf-8 -*-

"""
:copyright: Copyright (c) 2016 RadiaSoft LLC.  All Rights Reserved.
:license: http://www.apache.org/licenses/LICENSE-2.0.html
"""
import flask

app = flask.Flask(__name__)

import comsoljupyter.web.http
from comsoljupyter.web.orm import db

def run():
    orm.init()
    app.run()
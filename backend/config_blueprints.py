# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

from core.main import app

import subscriptions


def main():
    app.register_blueprint(subscriptions.blueprint, url_prefix='/inscricao')
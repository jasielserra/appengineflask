# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

from flask import Blueprint, render_template

blueprint = Blueprint('subscriptions', __name__, template_folder='templates')

@blueprint.route("/")
def form():
    return render_template('subscriptions_form.html')
from flask import Blueprint
auth_blueprint = Blueprint('Route', __name__)
from .Httpverbs import Httpverbs
auth_blueprint.add_url_rule(
    '/Common/<Func>',
    view_func=Httpverbs.as_view('Sup'),
    methods=['GET','POST','UPDATE','DELETE']
)


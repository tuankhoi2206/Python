from pyramid.view import view_config
from pyramid.compat import escape
from pyramid.response import Response
import logging

log = logging.getLogger(__name__)
from pyramid.view import (
    view_config,
    view_defaults
)


# Routing

@view_defaults(renderer='templates/home.jinja2')
class TutorialViews:
    def __init__(self, request):
        self.request = request

    @view_config(route_name='home')
    def home(self):
        return {'name': 'Home View'}

    @view_config(route_name='hello')
    def hello(self):
        return {'name': 'Hello View'}

# @view_config(route_name='home', renderer='templates/home.jinja2')
# def my_view(request):
#     log.debug('Some home')
#     session = request.session
#     if 'counter' in session:
#         session['counter'] += 1
#     else:
#         session['counter'] = 0
#     return {'name': 'Hello View'}
#
#
# # /howdy?name=alice which links to the next view
# @view_config(route_name='hello', renderer='templates/test.jinja2')
# def hello_view(request):
#     log.debug('Some message')
#     return dict()
#
#
# @view_config(route_name='hello_json', renderer='json')
# def hello_json(request):
#     return {
#         'project': 'Workspace_Python',
#         'project1': 'Workspace_Python1',
#         'project2': 'Workspace_Python2'
#     }
#
# @view_config(route_name='exception')
# def exception_view():
#     raise Exception()

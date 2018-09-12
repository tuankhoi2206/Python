from pyramid.config import Configurator
from pyramid.session import SignedCookieSessionFactory
my_session_factory = SignedCookieSessionFactory('itsaseekreet')

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    # Config templating with Jinja2
    config.include('pyramid_jinja2')
    # Config route and view
    # which register a route to match any URL path that begin with /
    # Let's point our web app at directory from which Pyrammid will serve some static assets.
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('hello', '/howdy')
    config.add_route('hello_json', '/hello_json')
    config.add_route('exception', '/problem')
    # config.add_route('test', '/test')

    config.set_session_factory(my_session_factory)
    config.scan()
    # WSGI Application Creation
    # WSGI is a protocol that allows servers to talk to Python applications.
    # Web container like Java Servlets
    return config.make_wsgi_app()

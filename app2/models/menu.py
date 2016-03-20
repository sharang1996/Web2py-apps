# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## Customize your APP title, subtitle and menus here
#########################################################################

response.logo = A(B('Blog Posts'),XML('&nbsp;'),
                  _class="navbar-brand",_href="http://www.web2py.com/",
                  _id="web2py-logo")
response.title = request.application.replace('_',' ').title()
response.subtitle = ''

## read more at http://dev.w3.org/html5/markup/meta.name.html
response.meta.author = myconf.get('app.author')
response.meta.description = myconf.get('app.description')
response.meta.keywords = myconf.get('app.keywords')
response.meta.generator = myconf.get('app.generator')

## your http://google.com/analytics id
response.google_analytics_id = None

#########################################################################
## this is the main application menu add/remove items as required
#########################################################################

response.menu = [
    (T('List'), False, URL('default', 'index'), []),
    (T('Create'), False, URL('default', 'create'), []),
    (T('Login'), False, URL('default','user'), []),
    (T('Sign Up'),False,URL('user/register'))
]

if auth.has_membership('managers'):
    response.menu.append((T('Manage'), False ,URL('default','manage')))
    


if "auth" in locals(): auth.wikimenu()

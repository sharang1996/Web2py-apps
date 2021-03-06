# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a sample controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
#########################################################################

def index():
    """
    example action using the internationalization operator T and flash
    rendered by views/default/index.html or views/generic.html

    if you need a simple wiki simply replace the two lines below with:
    return auth.wiki()
    """
    #response.flash = T("Hello World")
    #return {'message':'Hello World'}
    #return dict(message=T('hello from the other side!!'))
    #session.a=session.a+1
    #session.c=session.get('c',0) + 1
    #message=T("hi there!!  %s " % session.c)   #T for translate acc to user browser lang settings
    #return locals()
    #redirect(URL('other',args=[1,4,6],vars={'a':'test','b':78}))
    #redirect(URL('http://google.com')
    return locals()

def form1():
    form=SQLFORM.factory(Field('your_name',requires=IS_NOT_EMPTY()),
                        Field('birth_date','date')).process()
    if form.accepted:
        redirect(URL('other',vars={'your_name':form.vars.your_name}))
    return locals()


def other():
    #x=request.args
    #y=request.vars
    #return "this is the other page request.args= %s ,request.vars= %s" % (x,SPAN(y))
    message="welcome %s" % request.vars.your_name
    return locals()



def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    also notice there is http://..../[app]/appadmin/manage/auth to allow administrator to manage users
    """
    return dict(form=auth())


@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()

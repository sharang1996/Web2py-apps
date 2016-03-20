def hello(): 
    return "hello from the other side!!!"
def dict():
    a=1
    b=2
    return locals()
def htmltest():
    x=request.env.http_accept_language
    y=request.args
    return "<html><body><h1> %s hello world!!!  %s </h1></body></html>" % (x,y)
def new():
    z=request.vars
    import cgi
    return "<html><body><h1>%s</h1></body></html>" % cgi.escape(str(z))

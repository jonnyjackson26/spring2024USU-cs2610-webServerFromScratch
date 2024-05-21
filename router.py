from endpoints import projects, about, experience, home
from Response import Response
import datetime

def router(req):
    if req.uri=="/projects":
        return projects(req)
    elif req.uri=='/about' or req.uri=='/info':
        return about(req)
    elif req.uri=='/experience':
        return experience(req)
    elif req.uri=='/home' or req.uri=='/':
        return home(req)
    else:
        return Response(
            version='HTTP/1.1',
            code=404,
            reason='Not found',
            headers={
                "Connection":"close",
                "Server":"Jonnys cool sever",
                "Cache-control":'no-cache',
                "Date":str(datetime.datetime.today()),
                "Content-Type":"text/html",
                "Content-Length":"23"
            },
            text="<h1>404 Error: Page not found</h1>"
        )
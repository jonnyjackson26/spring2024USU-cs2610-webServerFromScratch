import datetime
from Response import Response

def projects(req):
    response_text = ""
    with open('templates/projects.html') as f:
        response_text=f.read()
    return Response(
                version='HTTP/1.1',
                code=200,
                reason='ok',
                headers={
                    "Connection":"close",
                    "Server":"Jonnys cool sever",
                    "Cache-control":'no-cache',
                    "Date":str(datetime.datetime.today()),
                    "Content-Type":"text/html",
                    "Content-Length":len(response_text)
                },
                text=response_text
            )

def about(req):
    response_text = ""
    with open('templates/about.html') as f:
        response_text=f.read()
    return Response(
                version='HTTP/1.1',
                code=200,
                reason='ok',
                headers={
                    "Connection":"close",
                    "Server":"Jonnys cool sever",
                    "Cache-control":'no-cache',
                    "Date":str(datetime.datetime.today()),
                    "Content-Type":"text/html",
                    "Content-Length":len(response_text)
                },
                text=response_text
            )

def experience(req):
    response_text = ""
    with open('templates/experience.html') as f:
        response_text=f.read()
    return Response(
                version='HTTP/1.1',
                code=200,
                reason='ok',
                headers={
                    "Connection":"close",
                    "Server":"Jonnys cool sever",
                    "Cache-control":'no-cache',
                    "Date":str(datetime.datetime.today()),
                    "Content-Type":"text/html",
                    "Content-Length":len(response_text)
                },
                text=response_text
            )


def home(req):
    response_text = ""
    with open('templates/index.html') as f:
        response_text=f.read()
    return Response(
                version='HTTP/1.1',
                code=200,
                reason='ok',
                headers={
                    "Connection":"close",
                    "Server":"Jonnys cool sever",
                    "Cache-control":'no-cache',
                    "Date":str(datetime.datetime.today()),
                    "Content-Type":"text/html",
                    "Content-Length":len(response_text)
                },
                text=response_text
            )
import datetime
from Response import Response

def compose(end_result_function, middleware_factory_list):
    chain=end_result_function
    for middleware in middleware_factory_list:
        chain=middleware(chain)
    return chain

def logging_middleware_factory(next):
    def middleware(request):
        print(f"Request received: {request.method} {request.uri}")
        response =  next(request)
        print(f"{response.code} {response.reason}")
        return response
    return middleware


def static_files_middleware_factory(next): #/code.js /styles.css
    def middleware(req):
        uri="static"+req.uri
        #print(uri)
        #attempt to read req.uri
                #if it doesnt exist return 404
                #if it does, respond with 200 and use contents in file as text for response
        if "." in uri:
            try:
                with open(uri) as f:
                    response_text=f.read()
                    if "css" in uri:
                        contentType='text/css'
                    elif "js" in uri:
                        contentType="text/javascript"
                    else:
                        raise FileNotFoundError()
                    return Response(
                        version='HTTP/1.1',
                        code='200',
                        reason='ok',
                        headers={
                            "Connection":"close",
                            "Server":"Jonnys cool sever",
                            "Cache-control":'no-cache',
                            "Date":str(datetime.datetime.today()),
                            "Content-Type":contentType,
                            "Content-Length":"23"
                        },
                        text=response_text
                    )
            except:
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
        resp = next(req)
        return resp
    return middleware


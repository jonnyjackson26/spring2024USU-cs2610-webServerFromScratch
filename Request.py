class Request:
    def __init__(
        self,
        method, #string
        uri, #string
        version, #string
        text, #string
        headers, #dict, the keys are the header names and values are the header values
    ):
        self.method = method
        self.uri = uri
        self.version = version
        self.text = text
        self.headers = headers

    def printDetails(self):
        headers=""
        for header in self.headers:
            headers=headers+header+" : "+header+"\n"
        h="method: "+self.method+"\n"+ \
        "uri: "+self.uri+"\n"+\
        "version: "+self.version+"\n" +\
        "text: "+self.text+"\n" +\
        "headers: "+headers
        print(h)
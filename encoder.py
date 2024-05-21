from Request import Request

def decode_request(http_string):  #takes string and returns request
    #split http string by newlines
    lines =http_string.split('\n')
    firstLine=lines[0].split(" ")
    method=firstLine[0]
    uri=firstLine[1]
    version=firstLine[2]

    headers={}
    for i in range(1,len(lines)-2):
        header=lines[i].split(":")
        headers[header[0]]=header[1]

    return Request(
        method=method,
        version=version,
        uri=uri,
        headers=headers, 
        text=""
    )

def encode_response(response):  #takes a resposne and returns string
    s=response.version+" "+str(response.code)+" "+response.reason+"\n"
    for i in response.headers:
         s=s+"'"+str(i)+"': '"+str(response.headers[i])+"'\n"

    #for the text:
    s=s+"\n\n"+response.text
    return s
    

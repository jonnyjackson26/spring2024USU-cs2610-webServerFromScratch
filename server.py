from Response import Response
from router import router
import socket
from encoder import decode_request,encode_response
from middleware import logging_middleware_factory, static_files_middleware_factory, compose

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(("127.0.0.1", 8000))
    s.listen()
    print("listening on port 8000")

    while True:
        connection, addr = s.accept()
        with connection:
            data = connection.recv(8192)
            if not data:
                connection.close()
                continue

            request=decode_request(str(data,"UTF-8"))

            middlewareList=[logging_middleware_factory,static_files_middleware_factory]
            middleware_chain=compose(router,middlewareList)
            resp=middleware_chain(request)

            response_data=encode_response(resp)
            #print(response_data)
            connection.send(bytes(response_data,"UTF-8"))


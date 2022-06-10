# Square : gRpc

A grpc service for calculating the square of a number.

## Generating supported file from .proto file

Use terminal to run command.

```bash
$ python -m grpc.tools.protoc --proto_path=. --python_out=. --grpc_python_out=. test.proto 

## Guidelines

Write a grpc server in python that has a grpc method called Square that takes a single float as a parameter and then returns back the square of that number.

https://grpc.io/docs/languages/python/basics/ <-- that should be more than enough

I like grpcurl more than grpc_cli cause grpcurl can work with SSH tunnels via the -plaintext flag

Verify it works via grpcurl ie grpcurl -plaintext  -d '{"arg1": 12345}'127.0.0.1:50051 something.something.something/something

For extra credit implement reflection so you can do something like grpcurl 127.0.0.1:50051 list

Next dockerize the python app.  for extra credit do it via docker-compose so you can do something like docker-compose up --build -d some_container

You might need help on this so let me know and also there's more after this, this is just the beginner blocks.  Eventually wire it up into envoy proy to go from grpc to grpcweb.  Thenspin up a frontend that communicates with it.

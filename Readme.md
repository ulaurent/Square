# Square : gRpc

A grpc service for calculating the square of a number.

## Generating supported file from .proto file

Use terminal to run command.

```bash
$ python -m grpc.tools.protoc --proto_path=. --python_out=. --grpc_python_out=. test.proto 
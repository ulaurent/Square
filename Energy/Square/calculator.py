import math

def square_number(x):
    y = math.sqrt(x)
    return y


# python -m grpc.tools.protoc --proto_path=. --python_out=. --grpc_python_out=. test.proto 
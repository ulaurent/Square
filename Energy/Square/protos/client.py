import grpc
import test_pb2
import test_pb2_grpc

# each client needs a stub to communicate with the service
def run():
    print("The client function")
    with grpc.insecure_channel('localhost:50052', options=(('grpc.enable_http_proxy', 0),)) as channel:
        print("The client function")
        stub = test_pb2_grpc.SquareServiceStub(channel)
        response = stub.squareNumber(test_pb2.Number(value = 2))
        print("The value is")
        print(response.responseA)


if __name__ == '__main__':
    run()
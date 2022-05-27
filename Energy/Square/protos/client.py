import grpc
import test_pb2
import test_pb2_grpc

# each client needs a stub to communicate with the service
def run():
    with grpc.insecure_channel('0.0.0.0:50052') as channel:
        stub = test_pb2_grpc.SquareServiceStub(channel)
        response = stub.squareNumber(test_pb2.Number(input = 2))
        print(response.responseA)


if __name__== '_main_':
    run()
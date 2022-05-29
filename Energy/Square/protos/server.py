
from concurrent import futures
import grpc
import test_pb2
import test_pb2_grpc


#create a class to define the server functions
#these functions will derive from the test_pb2_grpc.SquareService

class SquareServiceServicer(test_pb2_grpc.SquareServiceServicer):

    def squareNumber(self, request, context):
        responseA = request.input * request.input
        return test_pb2.Result(responseA = responseA)


def main():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=5))
    test_pb2_grpc.add_SquareServiceServicer_to_server(SquareServiceServicer(), server)
    print("Server Started!")
    server.add_insecure_port('[::]:50052')
    server.start()
    server.wait_for_termination()

main()

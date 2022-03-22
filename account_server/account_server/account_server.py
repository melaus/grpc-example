import logging
from concurrent.futures import ThreadPoolExecutor

import grpc
import account_pb2
import account_pb2_grpc

accounts = {
    123: account_pb2.GetAccountResponse(
        account_id=123,
        territory=account_pb2.Territory.GB,
        industry_ids=(90001, 90002),
    ),
    456: account_pb2.GetAccountResponse(
        account_id=456,
        territory=account_pb2.Territory.GB,
        industry_ids=(90003,),
        email="456@gmail",
    ),
    789: account_pb2.GetAccountResponse(
        account_id=789,
        territory=account_pb2.Territory.GB,
        industry_ids=(90004, 90005, 90006, 90007, 90008),
        email="456@gmail",
    ),
}

industry_ids = {
    123: (90001, 90002),
    456: (90003,),
    789: (90004, 90005, 90006, 90007, 90008),
}


class Account(account_pb2_grpc.AccountServicer):
    """
    Account creates a server (`AccountServicer`) implementation.
    The client will use the `AccountStub` to invoke `GetAccount`
    """

    def GetAccount(self, request: account_pb2.GetAccountRequest, context):
        return accounts[request.account_id]

    def StreamIndustryIds(self, request: account_pb2.StreamIndustryIdsRequest, context):
        for industry_id in industry_ids[request.account_id]:
            yield account_pb2.StreamIndustryIdsResponse(industry_id=industry_id)


def serve():
    server = grpc.server(ThreadPoolExecutor(max_workers=10))
    account_pb2_grpc.add_AccountServicer_to_server(Account(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    serve()

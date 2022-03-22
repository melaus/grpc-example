import logging
from typing import Iterator

import grpc
import account_pb2
import account_pb2_grpc


def get_account(stub: account_pb2_grpc.AccountStub, account_id: int):
    response: account_pb2.GetAccountResponse = stub.GetAccount(
        account_pb2.GetAccountRequest(account_id=account_id)
    )

    # This demonstrates how we can check whether an optional field is set
    # Using the updated contract means we have access to the new field
    if response.join_year == 2020:
        has_email_field = response.HasField("email")
        print(f"has_email_field? {has_email_field}")
        print(response)
    else:
        print("Account has join year before 2020")


def stream_industry_ids(stub: account_pb2_grpc.AccountStub, account_id: int):
    responses: Iterator[account_pb2.StreamIndustryIdsResponse] = stub.StreamIndustryIds(
        account_pb2.StreamIndustryIdsRequest(account_id=account_id)
    )

    # We don't have to send everything in one go.
    # We can stream them and iterate over an iterator of responses
    # (thanks to HTTP/2).
    for response in responses:
        print(
            f"Industry id '{response.industry_id}' streamed for requested account '{account_id}'"
        )


if __name__ == "__main__":
    logging.basicConfig()
    with grpc.insecure_channel("localhost:50051") as channel:
        # We create a channel to the server.
        #
        # We then create an instance of the stub so that we can
        # call our RPC methods.
        stub = account_pb2_grpc.AccountStub(channel)

        # 1. Should return a `GetAccountResponse` of the given `account_id`
        print("GetAccount 123:")
        get_account(stub, 123)
        print()

        print("GetAccount 456:")
        get_account(stub, 456)
        print()
        print()

        # 2. Should stream a list of industry ids one by one
        print("StreamIndustryIds:")
        stream_industry_ids(stub, 789)
        print()

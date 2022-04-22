import asyncio
import account

from grpclib.client import Channel


async def main():
    channel = Channel(host="127.0.0.1", port=50051)
    service = account.AccountStub(channel)
    response = await service.get_account(account_id=123)
    print(response)

    async for response in service.stream_industry_ids(account_id=789):
        print(response)

    # don't forget to close the channel when done!
    channel.close()


if __name__ == "__main__":
    asyncio.run(main())

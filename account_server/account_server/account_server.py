import asyncio
import account
from grpclib.server import Server
from typing import AsyncIterator


accounts = {
    123: account.GetAccountResponse(
        account_id=123,
        territory=account.Territory.GB,
        industry_ids=[90001, 90002],
    ),
    456: account.GetAccountResponse(
        account_id=456,
        territory=account.Territory.GB,
        industry_ids=[90003],
        email="456@gmail",
    ),
    789: account.GetAccountResponse(
        account_id=789,
        territory=account.Territory.GB,
        industry_ids=[90004, 90005, 90006, 90007, 90008],
        email="456@gmail",
    ),
}

industry_ids = {
    123: (90001, 90002),
    456: (90003,),
    789: (90004, 90005, 90006, 90007, 90008),
}


class AccountService(account.AccountBase):
    async def get_account(self, account_id: int) -> account.GetAccountResponse:
        return accounts[account_id]

    async def stream_industry_ids(
        self, account_id: int
    ) -> AsyncIterator[account.StreamIndustryIdsResponse]:
        for industry_id in industry_ids[account_id]:
            yield account.StreamIndustryIdsResponse(industry_id)


async def main():
    server = Server([AccountService()])
    await server.start("127.0.0.1", 50051)
    await server.wait_closed()


if __name__ == "__main__":
    asyncio.run(main())

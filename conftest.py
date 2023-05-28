import pytest_asyncio
import pytest

from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine

from config import SQLALCHEMY_TEST_DATABASE_URI
from models import Base


@pytest_asyncio.fixture
async def fake_http_client():
    pass


@pytest_asyncio.fixture
async def fake_engine(request):
    engine = create_async_engine("1")
    async with engine.connect() as conn:

        await conn.run_sync(Base.metadata.create_all)
        await conn.commit()

        yield engine

        # yield 'aaaa'

        # await conn.run_sync(Base.metadata.drop_all)
        # await conn.commit()


# @pytest.fixture
# def test_govna(request):
#     request.cls.list_govna = [1, 2, 3]

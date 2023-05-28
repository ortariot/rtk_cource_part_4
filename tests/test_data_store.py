import pytest
import pytest_asyncio
from models import Users
import bcrypt

from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.exc import NoResultFound
from sqlalchemy.ext.asyncio import AsyncSession

# pytestmark = pytest.mark.asyncio


class TestDataStore:

    @pytest.mark.asyncio
    async def test_1(self, fake_engine):

        async with fake_engine.connect() as engine:
            async_sesion_factory = sessionmaker(
                engine,
                expire_on_commit=False,
                class_=AsyncSession
            )
            async with session.begin():
                pass

        # async with await fake_engine.begin() as session:
        #     user = Users(
        #         name='name',
        #         phone='phone',
        #         mail='mail',
        #         login='login',
        #         password=bcrypt.hashpw(
        #             'password'.encode(), bcrypt.gensalt()),)

        #     session.add(user)

        print('aaa')
        assert 4 == 3

    # @pytest.mark.usefixtures('test_govna')
    # def test_exemple(self):
    #     assert self.list_govna == [1, 2, 3]

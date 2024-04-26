from domain.api.RepositoryApi import RepositoryApi


# noinspection PyBroadException
class RepositoryImpl(RepositoryApi, ):
    dataBase = None

    def __init__(self, dataBase):
        self.dataBase = dataBase

    def init(self) -> bool:
        try:
            self.dataBase.init()
            return True
        except:
            return False

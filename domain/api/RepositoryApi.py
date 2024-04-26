from abc import ABC, abstractmethod


class RepositoryApi(ABC):
    @abstractmethod
    def init(self):
        pass

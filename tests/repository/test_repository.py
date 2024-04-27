import unittest

from domain.impl.Repository import Repository
from tests.repository.test_data_repository import FakeDataBase


class Test_Repository(unittest.TestCase):
    def _raise(param):
        raise Exception("Database error")

    def test_repository_handles_errors(self):
        fake_db = FakeDataBase()

        fake_db.put_lambda = lambda a, b, c, d: self._raise()
        fake_db.delete_lambda = lambda a, b, c: self._raise()
        fake_db.select_lambda = lambda a, b: self._raise()
        fake_db.delete_all_lambda = lambda a, b: self._raise()

        repository = Repository(fake_db)

        repository.add_to_list("", "", "")
        repository.show_list("")
        repository.remove_from_list("","")
        repository.clear_list("")

        self.assertTrue(True)



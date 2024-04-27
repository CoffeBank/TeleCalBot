from typing import Optional


class FakeDataBase:
    init_lambda = lambda a: 0
    put_lambda = lambda a, b, c, d: 0
    delete_lambda = lambda a, b, c: True
    select_lambda = lambda a, b: ""
    delete_all_lambda = lambda a, b: True

    def init(self):
        self.init_lambda()

    def put(self, chat_id, username, string):
        self.put_lambda(chat_id, username, string)

    def delete(self, chat_id, string) -> bool:
        return self.delete_lambda(chat_id, string)

    def select(self, chat_id) -> Optional[str]:
        return self.select_lambda(chat_id)

    def delete_all(self, chat_id) -> Optional[bool]:
        return self.delete_all_lambda(chat_id)

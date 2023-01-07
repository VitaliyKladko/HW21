from entity.abstract_storage import AbstractStorage
from entity.exceptions import InvalidRequestError, UnknownStorage


class Request:
    def __init__(self, request_str: str, storages: dict[str, AbstractStorage]):
        split_request = request_str.lower().split(' ')
        if len(split_request) != 7 or not split_request[1].isdigit():
            # TODO: Ошибка "Неправильный запрос"
            raise InvalidRequestError

        self.amount = int(split_request[1])
        self.product = split_request[2]
        self.destination = split_request[6]
        self.departure = split_request[4]

        if self.departure not in storages or self.destination not in storages:
            # TODO: Ошибка 'Неизвестный склад'
            raise UnknownStorage

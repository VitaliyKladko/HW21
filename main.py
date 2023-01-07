from entity.store import Store
from entity.shop import Shop
from entity.request import Request
from entity.courier import Courier
from entity.exceptions import BaseError

shop = Shop(
    items={
        'печенька': 3,
        'ноут': 15,
    },
)

store = Store(
    items={
        'печенька': 10,
        'ноут': 20,
    },
)

storages = {
    'магазин': shop,
    'склад': store,
}


def main():
    while True:
        # TODO: Вывести содержимое складов
        for storage_name in storages:
            print(f'В {storage_name} хранится: {storages[storage_name].get_items()}')

        # TODO: Запросить у пользовател строку
        user_input = input(
            'Введите строку в формате "Доставить 3 печенька из склад в магазин".\n'
            'Введите "stop" или "стоп", чтобы остановить программу:\n'
        )

        if user_input in ('stop', 'стоп'):
            break

        # TODO: Обработать строку, проверить на ошибки, определить товар, количество, точки отправления и назначения
        try:
            request = Request(request_str=user_input, storages=storages)
            # TODO: Доставить товар
            courier = Courier(request=request, storages=storages)
            courier.move()
        except BaseError as error:
            print(error.message)


if __name__ == '__main__':
    main()

from Address import Address
from Mailing import Mailing


def main():

    sender_address = Address("123456", "Москва", "Ленинский проспект", 10, 20)
    recipient_address = Address("654321", "Санкт-Петербург", "Невский проспект", 15, 30)


    mailing = Mailing(
        to_address=recipient_address,
        from_address=sender_address,
        cost=1000.50,
        track="ABC12345"
    )


    print(f"Отправление {mailing.track} из {mailing.from_address.index}, {mailing.from_address.city}, "
          f"{mailing.from_address.street}, {mailing.from_address.house} - {mailing.from_address.apartment} "
          f"в {mailing.to_address.index}, {mailing.to_address.city}, {mailing.to_address.street}, "
          f"{mailing.to_address.house} - {mailing.to_address.apartment}. Стоимость {mailing.cost:.2f} рублей.")


if __name__ == "__main__":
    main()
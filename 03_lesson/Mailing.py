from Address import Address
class Mailing:
    def __init__(self, to_address: Address, from_address: Address, cost: float, track: str):
        self.to_address = to_address
        self.from_address = from_address
        self.cost = cost
        self.track = track

    def __str__(self):
        return (
            f"Почтовое отправление:\n"
            f"Отправлено от: {self.from_address}\n"
            f"Получено на: {self.to_address}\n"
            f"Стоимость: {self.cost:.2f}\n"
            f"Трек-код: {self.track}"
        )

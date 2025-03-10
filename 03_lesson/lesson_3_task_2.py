from smartphone import Smartphone

catalog = [
    Smartphone("Apple", "iPhone 13 Pro Max", "+79991234567"),
    Smartphone("Samsung", "Galaxy S22 Ultra", "+79876543210"),
    Smartphone("Xiaomi", "Mi 11 Ultra", "+79123456789"),
    Smartphone("Huawei", "P50 Pro", "+79201234567"),
    Smartphone("OnePlus", "9 Pro", "+79345678901")
]


for phone in catalog:
    print(phone)
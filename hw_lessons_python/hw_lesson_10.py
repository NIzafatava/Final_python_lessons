# # 1
#
# class Auto:
#
#     def __init__(self, brand, age, mark, color=None, weight=None):
#         self.brand = brand
#         self.age = age
#         self.mark = mark
#         self.color = color
#         self.weight = weight
#
#     def move(self):
#         print('move')
#
#     def stop(self):
#         print('stop')
#
#     def birthday(self):
#         print(self.age + 1)
#
#
# auto = Auto('kia', 12, 'kvs')
# print(Auto.move(auto))
# print(Auto.birthday(auto))
#
#
#
# # 2
#
#
# import time
#
#
# class Truck(Auto):
#
#     def __init__(self, max_load):
#         self.max_load = max_load
#
#     def load(self):
#         time.sleep(1)
#         print('load')
#         time.sleep(1)
#
#     def move(self):
#         super().move()
#         print('Attention, move')
#
# class Car(Auto):
#
#     def __init__(self, max_speed):
#         self.max_speed = max_speed
#
#     def move(self):
#         super().move()
#         print(f'move, max speed is {self.max_speed}')
#
#
# my_truck = Truck(4)
# my_car = Car(12)
# print(my_car.max_speed)
# print(my_truck.max_load)
# Auto.move(my_car)
# my_car.move()
# my_truck.move()


# 3



"""
Написать программу телефонная книга используя классы.
Написать класс телефонной книги, который хранит список контактов.
Он должен иметь возможность искать контакты по имени и по телефону
(два разных метода), добавлять новые контакты и удалять контакты по имени или телефону.
Контакты реализовать в виде объектов класса Контакт. Данные телефонной книги хранить в json файле.
"""
import json


class Contact:
    def __init__(self, name: str, phone: str) -> None:
        self.name = name
        self.phone = phone

    # def __str__(self):
    #     return f"{self.name}: {self.phone}"

    def __repr__(self):
        # return f'{self.name}: {self.phone}'
        return f'Contact({self.name}: {self.phone})'


class PhoneBook:
    def __init__(self, file_name: str) -> None:
        self.file_name = file_name
        with open(file_name) as file:
            list_of_dicts = json.load(file)
            self.contacts: list[Contact] = [Contact(**contact_dict) for contact_dict in list_of_dicts]

    def find_name(self, name: str) -> Contact | None:
        for contact in self.contacts:
            if contact.name == contact:
                return contact

    def find_phone(self, phone: str) -> Contact | None:
        for contact in self.contacts:
            if contact.phone == phone:
                return contact

    def add_contact(self, contact: Contact) -> Contact | None:
        if not self.find_name(contact.name):
            self.contacts.append(contact)
            return Contact

    def _delete_contact(self, contact: Contact | None) -> Contact | None:
        if contact is not None:
            self.contacts.remove(contact)
            return contact

    def delete_by_name(self, name: str) -> Contact | None:
        contact = self.find_by_name(name)
        return self._delete_contact(contact)

    def delete_by_phone(self, phone: str) -> Contact | None:
        contact = self.find_by_phone(phone)
        return self._delete_contact(contact)

    def save_to_file(self):
        with open(self.file_name, "w") as file:
            # contacts_list_of_dicts: list[dict] = [
            #     vars(contact) for contact in self.contacts
            # ]
            json.dump(self.contacts, file, indent=4, default=vars)


my_phone_book = PhoneBook("my_phone_book.json")
contacts = [
    Contact("Joe", "+375000000000"),
    Contact("Ann", "+375000000001"),
    Contact("Jack", "+375000000002"),
    Contact("Nick", "+375000000003"),
    Contact("Dan", "+375000000004"),
    Contact("Dan", "+375000000004"),
]
for contact in contacts:
    added_contact = my_phone_book.add_contact(contact)
    print(f"{contact} is added") if added_contact else print(f"{contact} is already in the book")
#
#
phones = ["+375000000002", "000"]
for phone in phones:
    contact = my_phone_book.find_by_phone(phone)
    if contact is not None:
        print(f"found by phone {contact}")
    else:
        print(f"{phone} not found")

    contact = my_phone_book.delete_by_phone(phone)
    if contact is not None:
        print(f"deleted by phone: {contact}")
    else:
        print(f"{phone} not found")
#
#
names = ["Dan", "Egor"]
for name in names:
    contact = my_phone_book.find_by_name(name)
    if contact is not None:
        print(f"found by name {contact}")
    else:
        print(f"{name} not found")

    contact = my_phone_book.delete_by_name(name)
    if contact is not None:
        print(f"deleted by name: {contact}")
    else:
        print(f"{name} not found")

print(my_phone_book.contacts)
my_phone_book.save_to_file()


contact = Contact("Ann", "+375000000001")
print(vars(contact))
print(contact.__dict__)



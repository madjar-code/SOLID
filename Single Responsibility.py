# Принцип единственной ответственности
from typing import (
    Dict,
    TypeAlias,
    NoReturn,
)

PhoneNumberType: TypeAlias = str
NameType: TypeAlias = str


class TelephoneDirectory:
    def __init__(self):
        self.phone_directory: \
            Dict[NameType, PhoneNumberType] = dict()

    def add_entry(self, name: NameType, number: PhoneNumberType) -> None:
        self.phone_directory[name] = number

    def delete_entry(self, name: NameType) -> None | NoReturn:
        self.phone_directory.pop(name)

    def update_entry(self, name: NameType, number: PhoneNumberType) -> None:
        self.phone_directory[name] = number

    def lookup_number(self, name) -> PhoneNumberType | NoReturn:
        return self.phone_directory[name]

    """ !!! Нарушение прицинипа единственности ответственности """
    def save_to_file(self, file_name: str, location: str) -> None:
        # код для сохранения phone_directory в файл
        pass

    def persist_to_database(self, database_details: str) -> None:
        # создание записей телефонного справочника в БД
        pass

    def __str__(self) -> str:
        ret_dct = ""
        for key, value in self.phone_directory.items():
            ret_dct += f'{key}: {value}\n'
        return ret_dct


# Определение классов согласно данному принципу
class PersistToDatabase:
    def __init__(self, object_to_persist:\
            TelephoneDirectory) -> None:
        pass


class SaveToFile:
    def __init__(self, object_to_save:\
            TelephoneDirectory) -> None:
        pass
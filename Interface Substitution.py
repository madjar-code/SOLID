# Принцип разделения интерфейсов: ни один клиент не должен
# зависеть от методов, которые он не использует

# Нужно делать небольшие интерфейсы с небольшим 
# количеством абстрактным методов
from abc import abstractmethod


# ! Нарушение принципа разделения интерфейсов:
# class CommunicationDevice:
#     @abstractmethod
#     def make_calls():
#         pass

#     @abstractmethod
#     def send_sms():
#         pass

#     @abstractmethod
#     def browse_internet():
#         pass


# class SmartPhone(CommunicationDevice):
#     def make_calls():
#         # реализация
#         pass

#     def send_sms():
#         # реализация
#         pass

#     def browse_internet():
#         # реализация
#         pass


# class LandlinePhone(CommunicationDevice):
#     def make_calls():
#         # реализация
#         pass

#     # Следующие два метода нам вовсе не нужны, но их надо указать
#     # Это и есть нарушение принципа разделения интерфейсов
#     def send_sms():
#         pass

#     def browse_internet():
#         pass


# Корректная реализация с несколькими интерфейсами
class CallingDevice:
    @abstractmethod
    def make_calls():
        pass


class MessagingDevice:
    @abstractmethod
    def send_sms():
        pass


class InternetBrowsingDevice:
    @abstractmethod
    def browse_internet():
        pass


class SmartPhone(CallingDevice,
                 MessagingDevice,
                 InternetBrowsingDevice):
    def make_calls():
        # реализация
        pass

    def send_sms():
        # реализация
        pass

    def browse_internet():
        # реализация
        pass


class LandlinePhone(CallingDevice):
    def make_calls():
        # реализация
        pass

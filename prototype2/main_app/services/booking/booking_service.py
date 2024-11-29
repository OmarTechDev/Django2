from main_app.repositories.register_booking import RegisterBooking
from main_app.services.service_interface import ServiceBaseInterface


class BookingService1(ServiceBaseInterface):

    def operate(self,data:dict)->dict:
        #logica de negocio

        repository = RegisterBooking()
        result=repository.register(data)
        return result
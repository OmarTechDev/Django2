from django.forms import model_to_dict

from main_app.models import Booking, Estate


class  RegisterBooking():
    def register(self,data:dict)->dict:
        print("entro a register book",data)
        estate = data.get('estate_id')
        print("aqui el estate", estate)
        if not estate.is_available:
            raise ValueError("The selected estate is not available.")

        estate.is_available = False
        estate.save()
        print("paso")
        booking = Booking.objects.create(**data)

        result =  model_to_dict(booking,exclude=['days'])
        result["estate"]= model_to_dict(estate)
        return result
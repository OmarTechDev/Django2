from django.forms import model_to_dict

from main_app.models import Estate


class RegisterEstate():

    def save_estate(self,data: dict)->dict:
        estate = Estate(**data)
        estate.save()
        return model_to_dict(estate,exclude=['is_available'])

    # def save_estate(self,data: dict)->dict:
    #     estate = model_to_dict(Estate(**data).save())
    #     return estate
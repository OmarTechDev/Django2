from django.db import models

class Estate(models.Model):
    name = models.CharField(max_length=255)
    rooms = models.IntegerField()
    bathrooms = models.IntegerField()
    floors = models.IntegerField()
    price = models.DecimalField(max_digits=10,decimal_places=2)
    is_available = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    #<Estate registro>
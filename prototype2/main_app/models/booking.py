from django.db import models
from main_app.models import Estate

class Booking(models.Model):
    register_date = models.DateField()
    days = models.IntegerField()
    total_amount = models.DecimalField(max_digits=10,decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()
    is_paid = models.BooleanField()
    estate_id = models.ForeignKey(
        Estate,
        on_delete=models.CASCADE,
        related_name="estates"
    )

    def __str__(self):
        return self.register_date
from django.contrib import admin
from .models import CarMake, CarModel, CarDealer, DealerReview


# Register your models here.

# CarModelInline class
admin.register(CarModel)
# CarModelAdmin class
admin.register(CarMake)
# CarMakeAdmin class with CarModelInline
admin.register(CarDealer)
admin.register(DealerReview)
# Register models here

from django.db import models
from django.utils.timezone import now


# Create your models here.

# <HINT> Create a Car Make model `class CarMake(models.Model)`:
# - Name
# - Description
# - Any other fields you would like to include in car make model
# - __str__ method to print a car make object


# <HINT> Create a Car Model model `class CarModel(models.Model):`:
# - Many-To-One relationship to Car Make model (One Car Make has many Car Models, using ForeignKey field)
# - Name
# - Dealer id, used to refer a dealer created in cloudant database
# - Type (CharField with a choices argument to provide limited choices such as Sedan, SUV, WAGON, etc.)
# - Year (DateField)
# - Any other fields you would like to include in car model
# - __str__ method to print a car make object


# <HINT> Create a plain Python class `CarDealer` to hold dealer data


# <HINT> Create a plain Python class `DealerReview` to hold review data
class CarMake(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    # Add any other fields you would like to include

    def __str__(self):
        return self.name


class CarModel(models.Model):
    CAR_TYPES = (
        ('Sedan', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'WAGON'),
        # Add any other types you would like to include
    )

    make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    dealer_id = models.IntegerField()
    type = models.CharField(max_length=10, choices=CAR_TYPES)
    year = models.DateField()
    # Add any other fields you would like to include

    def __str__(self):
        return f"{self.make} {self.name}"


class CarDealer:
    def __init__(self, address, city, state, zip, lat, long, name, id=None):
        self.id = id
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.lat = lat
        self.long = long
        self.name = name


class DealerReview:
    def __init__(self, dealership, name, purchase, review, purchase_date=None, car_make=None, car_model=None, car_year=None, id=None):
        self.id = id
        self.dealership = dealership
        self.name = name
        self.purchase = purchase
        self.review = review
        self.purchase_date = purchase_date or now().date()
        self.car_make = car_make
        self.car_model = car_model
        self.car_year = car_year

from django.db import models

# Create your models here.
# models are the 'table' part in sqlite3
# Documentation referred to : https://docs.djangoproject.com/en/2.2/topics/db/models/4
# intend to create four different classes (models) for Hatchback, Sedan, SUVs/MUVs and Van. All these will be columns.
# Maruti Suzuki Arena
class car(models.Model): # Each model is a Python class that subclasses django.db.models.Model.

    name = models.CharField(max_length=20, blank=False)
    price = models.IntegerField()
    mileage = models.FloatField() # all are instances of the appropriate Field class
    stock = models.IntegerField()
    wait_time = models.CharField(max_length=30, default="In stock, no waiting!")
    # name, price, ... are fields of the model and map to the respective database column

    class Meta: # it is used as a base class for other models, its fields will be added to those of the child class.
        abstract = True # This class isn’t going to ever be used in isolation so abstract keyword is being used

    def __str__(self):
    # It returns a string representation of any object. It is used when a model instance needs to be coerced and displayed as a plain string.
        return 'Name: {0} Price: {1} Mileage: {2} Stock: {3} Waiting period: {4}'.format(self.name, self.price,self.mileage,self.stock,self.wait_time)


class hatchback(car): # all the attributes of the car class are being inherited using meta inheritance
    # here we can define some more attributes specific to a particular model
    pass
class sedan(car):
    pass # keyword to do nothing

class SUVMUV(car):
    pass

class van(car):
    pass

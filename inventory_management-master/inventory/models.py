from django.db import models

# Create your models here.
# model is the 'table' part and we use sqlite3 here
# Documentation referred to : https://docs.djangoproject.com/en/2.2/topics/db/models/
class Device(models.Model): # Each model is a Python class that subclasses django.db.models.Model.

    type = models.CharField(max_length=200, blank=False)
    price = models.IntegerField()

    choices = (
        ('AVAILABLE', 'Item ready to be purchased'),
        ('SOLD', 'Item already purchased'),
        ('RESTOCKING', 'Item restocking in few days')
    )

    status = models.CharField(max_length=10, choices=choices, default='SOLD')
    issues = models.CharField(max_length=50, default="No Issues")

    class Meta: #  it is used as a base class for other models, its fields will be added to those of the child class.
        abstract = True

    def __str__(self):
        return 'Type: {0} Price: {1}'.format(self.type, self.price)

class Desktops(Device):
    pass

class Laptops(Device):
    pass

class Mobiles(Device):
    pass


# class Desktops(models.Model):
#     type = models.CharField(max_length=200, blank=False)
#     price = models.IntegerField()
#
#     choices = (
#         ('SOLD', 'Item already purchased'),
#         ('AVAILABLE', 'Item ready to be purchased'),
#         ('RESTOCKING', 'Item restocking in few days')
#     )
#
#     status = models.CharField(max_length=10, choices=choices, default='SOLD')
#     issues = models.CharField(max_length=50, default="No Issues")
#
#     def __str__(self):
#         return 'Type: {0} Price: {1}'.format(self.type, self.price)
#
#
# class Laptops(models.Model):
#     type = models.CharField(max_length=200, blank=False)
#     price = models.IntegerField()
#
#     choices = (
#         ('SOLD', 'Item already purchased'),
#         ('AVAILABLE', 'Item ready to be purchased'),
#         ('RESTOCKING', 'Item restocking in few days')
#     )
#
#     status = models.CharField(max_length=10, choices=choices, default='SOLD')
#     issues = models.CharField(max_length=50, default="No Issues")
#
#     def __str__(self):
#         return 'Type: {0} Price: {1}'.format(self.type, self.price)
#
#
# class Mobiles(models.Model):
#     type = models.CharField(max_length=200, blank=False)
#     price = models.IntegerField()
#
#     choices = (
#         ('SOLD', 'Item already purchased'),
#         ('AVAILABLE', 'Item ready to be purchased'),
#         ('RESTOCKING', 'Item restocking in few days')
#     )
#
#     status = models.CharField(max_length=10, choices=choices, default='SOLD')
#     issues = models.CharField(max_length=50, default="No Issues")
#
#     def __str__(self):
#         return 'Type: {0} Price: {1}'.format(self.type, self.price)

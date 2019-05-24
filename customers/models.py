from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    customer_phone = models.IntegerField()
    email = models.CharField(max_length=50)
    user_name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return str(self.id)

class Address(models.Model):
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    address =  models.TextField()
    pincode = models.IntegerField()
    city = models.CharField(max_length=50)
    state =  models.CharField(max_length=50)
    country =  models.CharField(max_length=50)

    def __str__(self):
        return str(self.customer_id.first_name)
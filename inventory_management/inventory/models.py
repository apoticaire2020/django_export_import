from typing import AbstractSet
from django.db import models

# Create your models here.
CATEGORY =(
   
    ('med' , 'med'),
    ('para' , 'para'),
    ('diet' , 'diet'),

)
FORME =(
   
    ('comprime' , 'comprime'),
    ('sirop' , 'sirop'),
    ('suppo' , 'suppo'),
    ('inj' , 'inj'),

)

class Product(models.Model):
    designation= models.CharField(max_length=20 , null=True)
    category=models.CharField(max_length=20 , choices=CATEGORY , null=True)
    forme=models.CharField(max_length=15 ,choices=FORME , null=True)
    ppv = models.FloatField(null=True)
    pph = models.FloatField(null=True)
    quantity = models.IntegerField(null=True)

    #class Meta:
    #    db_table = "med-converti"

    def __str__(self) -> str:
        return f'{self.designation}-{self.ppv}-{self.quantity}'


        
class Device(models.Model):
    type= models.CharField(max_length=20, blank=False)
    price = models.FloatField()

    class Meta:
        abstract = True
        

    def __str__(self) -> str:
        return 'Type:{0} Price:{1}'.format(self.type , self.price)
    

class Laptop(Device):
    pass


class Desktop(Device):
    pass


class Mobile(Device):
    pass


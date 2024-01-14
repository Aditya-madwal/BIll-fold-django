from django.db import models

# Create your models here.

class transactions(models.Model) :
    amount = models.IntegerField(blank=True)
    label = models.CharField( 
        max_length = 20, 
        choices = (('1','Income'),('2','Expense')), 
        default = '1',
        blank=True,
        )

    category = models.CharField(max_length=50,blank=True)

    def __str__(self):
        return f"{self.label} --> {self.amount}"

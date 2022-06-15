from django.db import models

# Create your models here.
class ProductB(models.Model):
    concate_name= models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return self.concate_name

class ProductA(models.Model):
    original_name = models.CharField(max_length=250, null=True, blank=True)
    product_b = models.ForeignKey(
        ProductB,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.original_name

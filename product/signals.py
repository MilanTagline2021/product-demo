import string    
import random
from django.dispatch import receiver
from django.db.models.signals import post_save
from product.models import ProductA, ProductB
 
 
@receiver(post_save, sender=ProductA)
def create_product_b(sender, instance, created, **kwargs):
	if created:
		ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 10))
		ProductB.objects.create(concate_name=str(ran))
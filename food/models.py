from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
class Item(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=200)
    item_price = models.IntegerField()
    item_image = models.CharField(max_length=500,default='https://imgs.search.brave.com/DPZzH5S4Yx7XboIZ_hAJtVWt_HAuIbeRX9zDQRzapYU/rs:fit:500:0:0:0/g:ce/aHR0cHM6Ly93d3cu/d2ViZnguY29tL3dw/LWNvbnRlbnQvdXBs/b2Fkcy8yMDIzLzA4/LzkwX2hvd190b19p/bWFnZV9wbGFjZWhv/bGRlcnMtMTAyNHg0/NjIucG5n')


    def __str__(self):
        return self.item_name

    def get_absolute_url(self):
        return reverse("food:detail", kwargs={"pk": self.pk})
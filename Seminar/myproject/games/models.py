from django.db import models

# Create your models here.

class Heads_or_tails(models.Model):
    side = models.CharField(max_length=5)
    datetimestamp = models.DateTimeField(auto_now=True)

    @staticmethod
    def get_N_last_flip(n):
        flips = Heads_or_tails.objects.order_by("-datetimestamp")[:n]
        heads = 0
        tails = 0
        for item in flips:
            if item.side == "Орел":
                heads += 1
            else:
                tails += 1
        return {"Орел": heads, "Решка": tails}
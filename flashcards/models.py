from django.db import models


class CardBundle(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=500)


class Card(models.Model):
    front_text = models.CharField(max_length=500)
    back_text = models.CharField(max_length=500)
    bundle = models.ForeignKey(CardBundle, on_delete=models.CASCADE)

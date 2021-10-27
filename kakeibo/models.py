from django.db import models


class ICategory(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class OCategory(models.Model):
    name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name

class Store(models.Model):
    name = models.CharField(max_length=30)
    memo = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.name


class Income(models.Model):
    category = models.ForeignKey(
        ICategory, related_name='incomes', on_delete=models.PROTECT)
    price = models.IntegerField()
    date = models.DateField()
    memo = models.TextField(null=True,blank=True)


class Outgo(models.Model):
    category = models.ForeignKey(
        OCategory, related_name='outgos', on_delete=models.PROTECT)
    price = models.IntegerField()
    date = models.DateField()
    store = models.ForeignKey(
        Store, related_name='outgos', on_delete=models.PROTECT, null=True, blank=True)
    memo = models.TextField(null=True, blank=True)

from django.db import models

# Create your models here.
class Area(models.Model):
    name = models.CharField(max_length=150)
    auther = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name
    
class Company(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    year = models.DateField(auto_now_add=True)
    auther = models.CharField(max_length=100)
    area = models.ForeignKey(Area,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name

class Building(models.Model):
    buildings = models.ForeignKey(Company,on_delete=models.CASCADE)
    area = models.ForeignKey(Area,on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    field = models.CharField(max_length=150)
    floor = models.IntegerField()
    childrens_playground = models.CharField(max_length=100)
    lift = models.IntegerField()
    auther = models.CharField(max_length=100)


    def __str__(self) -> str:
        return self.name
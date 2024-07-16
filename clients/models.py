from django.db import models

# Create your models here.
class Client(models.Model):
    code=models.CharField(max_length=200, unique=True, blank=True)
    name=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    phone=models.IntegerField(max_length=8)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    class Meta:
        managed = True
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'
    
    def __str__(self) -> str:
        return self.code